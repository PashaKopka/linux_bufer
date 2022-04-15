import time

from PyQt5 import QtWidgets, QtCore, QtGui
from pynput import keyboard


class ClipboardUnion(QtWidgets.QPushButton):

	def __init__(
			self,
			clipboard: QtGui.QClipboard,
			parent: QtWidgets.QWidget,
			parent_window: QtWidgets.QWidget,
	):
		super().__init__(parent)
		self.clicked.connect(self._paste)
		self._clipboard: QtGui.QClipboard = clipboard
		self._text: str = self._clipboard.text()

		# need to paste image
		self._image = self._clipboard.image() if not self._clipboard.pixmap().isNull() else None
		# need to show image in ui
		self._pixel_map = self._clipboard.pixmap() if not self._clipboard.pixmap().isNull() else None
		# list of urls to selected files
		self._files_urls = [x.path() for x in self._clipboard.mimeData().urls()]

		self._create_widget()
		self._parent_window = parent_window  # Need parent window to hiding it

	def _paste(self) -> None:
		"""
		paste clipboard data
		hide main window and then use shortcut <Ctrl>+V
		may be problems if is another shortcut in system for this function
		"""
		self._parent_window.hide_window()
		self._update_clipboard()

		keyboard_controller = keyboard.Controller()
		time.sleep(.01)  # Time to window hiding

		# emulate <Ctrl>+V pressing
		with keyboard_controller.pressed(keyboard.Key.ctrl):
			keyboard_controller.press('v')
			keyboard_controller.release('v')

	def _update_clipboard(self) -> None:
		"""
		updates last clipboard element
		it sets data in clipboard (like you use <Ctrl>+C)
		and then you can paste this data
		"""
		if self._files_urls:
			data = QtCore.QMimeData()
			urls = [QtCore.QUrl.fromLocalFile(x) for x in self._files_urls]
			data.setUrls(urls)
			self._clipboard.setMimeData(data)
		elif self._text:
			self._clipboard.setText(self._text)
		elif self._pixel_map:
			self._clipboard.setImage(self._image)
		else:
			raise TypeError('Now supports only text, image and files')

	def _create_widget(self) -> None:
		"""normalize union: sets standard styles, sets showing text or image"""
		if self._files_urls:
			# if user copy file
			file_names = [x.rsplit('/', 1)[-1] for x in self._files_urls]
			self._create_standard_clipboard_union()
			self.text.setText('\n'.join(file_names))
			self._set_application_icon()

		elif self._text:
			# set standard styles for union
			self._create_standard_clipboard_union()
			self.text.setText(self._text.replace('\t', '    '))
			self._set_application_icon()

		elif self._image:
			# if user copy image
			# TODO add function of saving image
			# TODO need to change from standard clipboard union to image clipboard union
			self._set_standard_styles(text_align='center')

			# set icon
			icon = QtGui.QIcon(self._pixel_map)
			self.setIcon(icon)
			self.setIconSize(QtCore.QSize(200, 90))

		else:
			raise TypeError('Now supports only text, image and files')

	def _set_application_icon(self):
		"""
		Sets icon to self.logo
		it`s icon of application, from which was copied data
		"""
		# TODO Wayland
		# TODO Problem with Slack, maybe something else

		import gi
		gi.require_version('Wnck', '3.0')
		gi.require_version('Gtk', '3.0')
		from gi.repository import Wnck

		current_screen = Wnck.Screen.get_default()
		current_screen.force_update()

		active_window = current_screen.get_active_window()
		icon_of_active_window = active_window.get_icon()
		image_binary_data = icon_of_active_window.read_pixel_bytes().get_data()

		# format that equals to GdkPixbuf
		image = QtGui.QImage(image_binary_data, 32, 32, QtGui.QImage.Format.Format_RGBA8888)
		icon_pixmap = QtGui.QPixmap().fromImage(image)
		self.logo.setPixmap(icon_pixmap)

	def _create_standard_clipboard_union(self) -> None:
		self.setObjectName('clipboard_union')
		self.setMinimumSize(QtCore.QSize(0, 100))
		self.setMaximumSize(QtCore.QSize(16777215, 100))
		self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.setStyleSheet(
			"QPushButton{\n"
			"    border: 2px solid #313131;\n"
			"    color: #fff;\n"
			"    border-radius: 10px;\n"
			"    background-color: #414141;\n"
			"    text-align:left top;\n"
			"    padding: 21px 70px 21px 20px;\n"
			"}\n"
			"\n"
			"QPushButton:hover{\n"
			"    border: 2px solid #08ffc8;\n"
			"}\n"
			"\n"
			"QPushButton:pressed{\n"
			"    background-color: #313131;\n"
			"    border: 2px solid #08ffc8;\n"
			"}"
		)

		self.horizontal_layout = QtWidgets.QHBoxLayout(self)
		self.horizontal_layout.setContentsMargins(0, 0, 0, 0)

		self.props = QtWidgets.QWidget(self)
		self.props.setMinimumSize(QtCore.QSize(62, 0))
		self.props.setMaximumSize(QtCore.QSize(40, 16777215))
		self.props.setStyleSheet("margin: 0px 10px 0 0;")

		self.verticalLayout = QtWidgets.QVBoxLayout(self.props)
		self.verticalLayout.setContentsMargins(0, 7, 0, 10)
		self.verticalLayout.setSpacing(0)

		self.datetime = QtWidgets.QLabel(self.props)
		self.font = QtGui.QFont()
		self.font.setPointSize(9)
		self.datetime.setFont(self.font)
		self.datetime.setStyleSheet("color: #fff;")
		self.datetime.setAlignment(QtCore.Qt.AlignCenter)
		time_string = time.strftime('%H:%M', time.localtime())
		self.datetime.setText(time_string)

		self.verticalLayout.addWidget(self.datetime)

		self.logo = QtWidgets.QLabel(self.props)
		self.logo.setMinimumSize(QtCore.QSize(32, 32))
		self.logo.setText("")

		self.verticalLayout.addWidget(self.logo)
		self.horizontal_layout.addWidget(self.props)

		self.text = QtWidgets.QLabel(self)
		self.text.setMinimumSize(QtCore.QSize(150, 100))
		self.text.setStyleSheet(
			"color: #fff;\n"
			"text-align:left top;\n"
			"padding: 22px 20px 22px 10px;"
		)
		self.text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.text.setWordWrap(True)

		self.horizontal_layout.insertWidget(0, self.text)

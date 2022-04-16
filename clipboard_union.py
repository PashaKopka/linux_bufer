import time
import abc

import validators
from PyQt5 import QtWidgets, QtCore, QtGui
from pynput import keyboard


class ClipboardUnion(QtWidgets.QPushButton):
	# can`t use AbstractClipboardUnion(ABC)

	def __init__(self, parent: QtWidgets.QWidget):
		super().__init__(parent)

	def paste(self):
		"""
		paste clipboard data
		hide main window and then use shortcut <Ctrl>+V
		may be problems if is another shortcut in system for this function
		"""
		self._parent_window.hide_window()
		self.update_clipboard()

		keyboard_controller = keyboard.Controller()
		time.sleep(.01)  # Time to window hiding

		# emulate <Ctrl>+V pressing
		with keyboard_controller.pressed(keyboard.Key.ctrl):
			keyboard_controller.press('v')
			keyboard_controller.release('v')

	def set_application_icon(self):
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

	@abc.abstractmethod
	def update_clipboard(self):
		pass

	@abc.abstractmethod
	def _create_widget(self):
		pass

	@abc.abstractmethod
	def _create_standard_clipboard_union(self):
		pass


class TextClipboardUnion(ClipboardUnion):

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget,
	):
		super().__init__(parent)
		self.clicked.connect(self.paste)
		self._clipboard: QtGui.QClipboard = clipboard
		self._parent_window = parent_window  # Need parent window to hiding it

		self._text: str = self._clipboard.text()

		self._create_widget()

	def update_clipboard(self) -> None:
		"""
		updates last clipboard element
		it sets data in clipboard (like you use <Ctrl>+C)
		and then you can paste this data
		"""
		self._clipboard.setText(self._text)

	def _create_widget(self) -> None:
		"""normalize union: sets standard styles, sets showing text or image"""
		self._create_standard_clipboard_union()
		self.text.setText(self._text.replace('\t', '    '))
		self.set_application_icon()

	def _create_standard_clipboard_union(self) -> None:
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
		self.logo.setAlignment(QtCore.Qt.AlignCenter)
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


class ImageClipboardUnion(ClipboardUnion):
	"""Image clipboard union if user copied image or make screenshot"""

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget
	):
		super().__init__(parent)
		self.clicked.connect(self.paste)
		self._parent: QtWidgets.QWidget = parent
		self._clipboard = clipboard

		# need to paste image
		self._image = self._clipboard.image()
		# need to show image in ui
		self._pixel_map = self._clipboard.pixmap()

		self._create_widget()
		self._parent_window = parent_window  # Need parent window to hiding it

	def update_clipboard(self):
		self._clipboard.setImage(self._image)

	def _create_widget(self):
		# TODO add function of saving image
		self._create_standard_clipboard_union()

		# set icon
		size = QtCore.QSize(262, 160)
		self._pixel_map = self._pixel_map.scaled(size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.image.setMinimumSize(size.width(), size.height())
		self.image.setMaximumSize(size.width(), size.height())
		self.image.setPixmap(self._pixel_map)

	def _create_standard_clipboard_union(self):
		self.setEnabled(True)
		self.setMinimumSize(QtCore.QSize(139, 200))
		self.setMaximumSize(QtCore.QSize(280, 200))
		self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.setStyleSheet(
			"QPushButton{\n"
			"    border: 2px solid #313131;\n"
			"    color: #fff;\n"
			"    border-radius: 10px;\n"
			"    background-color: #414141;\n"
			"}\n"
			"\n"
			"QPushButton:hover{\n"
			"    border: 2px solid #08ffc8;\n"
			"}\n"
			"\n"
			"QPushButton:pressed{\n"
			"    background-color: #313131;\n"
			"    border: 2px solid #08ffc8;\n"
			"}")

		self.verticalLayout = QtWidgets.QVBoxLayout(self)
		self.verticalLayout.setContentsMargins(9, 9, 9, 9)
		self.verticalLayout.setSpacing(6)

		self.datetime = QtWidgets.QLabel(self)
		self.datetime.setMaximumSize(QtCore.QSize(16777215, 10))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.datetime.setFont(font)
		self.datetime.setStyleSheet("color: #fff;")
		self.datetime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		time_string = time.strftime('%H:%M', time.localtime())
		self.datetime.setText(time_string)

		self.verticalLayout.addWidget(self.datetime)

		self.image = QtWidgets.QLabel(self)
		self.image.setMinimumSize(QtCore.QSize(0, 0))
		self.image.setStyleSheet(
			"color: #fff;\n"
			"text-align: center;\n")
		self.image.setText("")
		self.image.setAlignment(QtCore.Qt.AlignCenter)
		self.image.setWordWrap(True)

		self.verticalLayout.addWidget(self.image)
		spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		self.verticalLayout.addItem(spacerItem)


class FileClipboardUnion(ClipboardUnion):
	"""Image clipboard union if user copied file"""

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget
	):
		super().__init__(parent)
		self.clicked.connect(self.paste)
		self._parent: QtWidgets.QWidget = parent
		self._clipboard = clipboard

		# list of urls to selected files
		self._files_urls = [x.path() for x in self._clipboard.mimeData().urls()]

		self._create_widget()
		self._parent_window = parent_window  # Need parent window to hiding it

	def update_clipboard(self):
		data = QtCore.QMimeData()
		urls = [QtCore.QUrl.fromLocalFile(x) for x in self._files_urls]
		data.setUrls(urls)
		self._clipboard.setMimeData(data)

	def _create_widget(self):
		file_names = [x.rsplit('/', 1)[-1] for x in self._files_urls]
		self._create_standard_clipboard_union()
		self.text.setText('\n'.join(file_names))

	def _create_standard_clipboard_union(self):
		self.setMinimumSize(QtCore.QSize(0, 100))
		self.setMaximumSize(QtCore.QSize(16777215, 100))
		self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.setStyleSheet(
			"QPushButton{\n"
			"    border: 2px solid #313131;\n"
			"    color: #fff;\n"
			"    border-radius: 10px;\n"
			"    background-color: #414141;\n"
			"}\n"
			"\n"
			"QPushButton:hover{\n"
			"    border: 2px solid #08ffc8;\n"
			"}\n"
			"\n"
			"QPushButton:pressed{\n"
			"    background-color: #313131;\n"
			"    border: 2px solid #08ffc8;\n"
			"}")
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setContentsMargins(10, 0, 10, 7)

		self.text = QtWidgets.QLabel(self)
		self.text.setMinimumSize(QtCore.QSize(150, 100))
		self.text.setStyleSheet(
			"color: #fff;\n"
			"text-align:left top;\n"
			"padding: 22px 20px 22px 0px;")
		self.text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.text.setWordWrap(True)

		self.gridLayout.addWidget(self.text, 0, 0, 1, 1)

		self.props = QtWidgets.QWidget(self)
		self.props.setMinimumSize(QtCore.QSize(60, 0))
		self.props.setMaximumSize(QtCore.QSize(40, 16777215))
		self.props.setStyleSheet("margin: 0;")

		self.verticalLayout = QtWidgets.QVBoxLayout(self.props)
		self.verticalLayout.setContentsMargins(0, 7, 0, 10)
		self.verticalLayout.setSpacing(0)

		self.datetime = QtWidgets.QLabel(self.props)
		font = QtGui.QFont()
		font.setPointSize(9)
		self.datetime.setFont(font)
		self.datetime.setStyleSheet("color: #fff;")
		self.datetime.setAlignment(QtCore.Qt.AlignCenter)

		self.verticalLayout.addWidget(self.datetime)

		self.logo = QtWidgets.QLabel(self.props)
		self.logo.setText("")
		self.logo.setScaledContents(False)
		self.logo.setAlignment(QtCore.Qt.AlignCenter)

		self.verticalLayout.addWidget(self.logo)

		self.gridLayout.addWidget(self.props, 0, 1, 1, 1)

		self.line = QtWidgets.QFrame(self)
		self.line.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.line.setStyleSheet("background-color: #08ffc8;")
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 1, 0, 1, 2)


class LinkClipboardUnion(TextClipboardUnion):
	pass


class ClipboardUnionFactory:

	def __init__(
			self,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget,
			layouts: dict[str, QtWidgets.QWidget]
	):
		self._clipboard = clipboard
		self._parent_window = parent_window
		self._layouts = layouts

		self._data: list = []  # can`t use set because QImage is unhashable object

		self._clipboard.dataChanged.connect(self.create_clipboard_union)

	def create_clipboard_union(self):
		file_urls, image, text = self._get_data_from_clipboard()

		if text in self._data or image in self._data or file_urls in self._data:
			# if data already in clipboard, skip it
			pass
		else:
			# add union to all_unions_scrollarea_content

			if self._clipboard.mimeData().urls():
				# if we have url in urls list -> user copied file
				self._data.append(file_urls)
				self._create_clipboard_union(self._layouts['all_unions'], FileClipboardUnion)
				self._create_clipboard_union(self._layouts['file'], FileClipboardUnion)

			elif not self._clipboard.pixmap().isNull():
				# if copied data is image
				self._data.append(image)
				self._create_clipboard_union(self._layouts['all_unions'], ImageClipboardUnion)
				self._create_clipboard_union(self._layouts['image'], ImageClipboardUnion)

			elif text:
				if validators.url(text):
					# if text looks like link
					self._create_clipboard_union(self._layouts['all_unions'], LinkClipboardUnion)
					self._create_clipboard_union(self._layouts['link'], LinkClipboardUnion)
				else:
					# just simple text
					self._create_clipboard_union(self._layouts['all_unions'], TextClipboardUnion)
					self._create_clipboard_union(self._layouts['text'], TextClipboardUnion)

				self._data.append(text)

			else:
				raise TypeError('Now supports only text, image and files')

	def _create_clipboard_union(self, parent: QtWidgets.QWidget, union_class: type(ClipboardUnion)):
		"""
		:param parent:
		:param union_class: link to class that you want to create
		:return:
		"""
		layout = parent.layout()
		union = union_class(parent, self._clipboard, self._parent_window)
		layout.insertWidget(0, union)
		self._append_unions_to_all_unions(union)

	def _append_unions_to_all_unions(self, union: ClipboardUnion):
		self._parent_window.all_unions.add(union)

	def _get_data_from_clipboard(self):
		text = self._clipboard.text()
		image = self._clipboard.image()
		file_urls = [x.path() for x in self._clipboard.mimeData().urls()]
		return file_urls, image, text

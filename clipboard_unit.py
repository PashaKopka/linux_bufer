import time
import abc

import validators
from PyQt5 import QtWidgets, QtCore, QtGui
from pynput import keyboard

from config import HIDING_TIME
from details_window import DetailsWindow


class ClipboardUnit(QtWidgets.QPushButton):
	# can`t use AbstractClipboardUnit(ABC)

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			parent_window: QtWidgets.QWidget
	):
		super().__init__(parent)
		self._details_window = DetailsWindow(parent_window)
		self._parent_window = parent_window

	def paste(self) -> None:
		"""
		paste clipboard data
		hide main window and then use shortcut <Ctrl>+V
		may be problems if is another shortcut in system for this function
		"""
		self._parent_window.hide_window()
		self.update_clipboard()

		keyboard_controller = keyboard.Controller()
		time.sleep(HIDING_TIME)  # Time to window hiding

		# emulate <Ctrl>+V pressing
		with keyboard_controller.pressed(keyboard.Key.ctrl):
			keyboard_controller.press('v')
			keyboard_controller.release('v')

	def set_application_icon(self) -> None:
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
		self.application_ico.setPixmap(icon_pixmap)

	def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
		if e.button() == QtCore.Qt.MiddleButton:
			# show details window near the mouse cursor
			self._parent_window.dont_hide_window_this_time()
			position = QtGui.QCursor.pos()
			self._details_window.move(position)
			self._details_window.show_window()

		elif e.button() == QtCore.Qt.LeftButton:
			# if user click on left mouse button -> paste data
			if self._parent_window.is_window_active():
				self.paste()
			else:
				self._parent_window.activate_window()

	def hide_details_window(self):
		self._details_window.hide_window()

	@abc.abstractmethod
	def has_text(self, text: str) -> bool:
		"""it is function to check if unit has text inside"""
		pass

	@abc.abstractmethod
	def update_clipboard(self) -> None:
		"""if user choose unit then unit should set self.data clipboard"""
		pass

	@abc.abstractmethod
	def _create_widget(self) -> None:
		"""all widgets must create self, set styles and activate some functions"""
		pass

	@abc.abstractmethod
	def _create_standard_clipboard_unit(self) -> None:
		"""all widgets should create own styles, or copy realisation from parent"""
		pass


class TextClipboardUnit(ClipboardUnit):

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget,
	):
		super().__init__(parent, parent_window)
		self.clicked.connect(self.paste)
		self._clipboard: QtGui.QClipboard = clipboard

		self._text: str = self._clipboard.text()

		self._create_widget()

	def update_clipboard(self) -> None:
		"""
		updates last clipboard element
		it sets data in clipboard (like you use <Ctrl>+C)
		and then you can paste this data
		"""
		self._clipboard.setText(self._text)

	def has_text(self, text: str) -> bool:
		"""
		function using for searching for units
		if unit has text, that user typed, inside -> return True
		"""
		if text.lower() in self.text.text().lower():
			return True
		return False

	def get_text(self):
		"""refactor text"""
		return self._text.replace('\t', '    ')

	def _create_widget(self) -> None:
		"""normalize unit: sets standard styles, sets showing text or image"""
		self._create_standard_clipboard_unit()
		self.text.setText(self.get_text())
		self.set_application_icon()

	def _create_standard_clipboard_unit(self) -> None:
		self.setMinimumSize(QtCore.QSize(0, 132))
		self.setMaximumSize(QtCore.QSize(16777215, 132))
		self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.setStyleSheet(
			"QPushButton{\n"
			"	background-color: #585B64;\n"
			"	border-radius: 5px;\n"
			"}"
			"QPushButton:hover{\n"
			"	border: 2px solid #FD7013;\n"
			"}")

		self.vertical_layout = QtWidgets.QVBoxLayout(self)
		self.vertical_layout.setContentsMargins(0, 0, 0, 0)
		self.vertical_layout.setSpacing(0)

		self.unit_info = QtWidgets.QWidget(self)
		self.unit_info.setMinimumSize(QtCore.QSize(0, 25))
		self.unit_info.setMaximumSize(QtCore.QSize(16777215, 25))

		font = QtGui.QFont()
		font.setPointSize(8)
		self.unit_info.setFont(font)

		self.unit_info_layout = QtWidgets.QHBoxLayout(self.unit_info)
		self.unit_info_layout.setContentsMargins(2, 0, 9, 0)
		self.unit_info_layout.setSpacing(0)

		self.unit_info_text_ico_label = QtWidgets.QLabel(self.unit_info)
		self.unit_info_text_ico_label.setMinimumSize(QtCore.QSize(25, 25))
		self.unit_info_text_ico_label.setMaximumSize(QtCore.QSize(25, 25))
		self.unit_info_text_ico_label.setText("")
		self.unit_info_text_ico_label.setPixmap(QtGui.QPixmap("interface/../sources/images/text-icon.svg"))

		self.unit_info_layout.addWidget(self.unit_info_text_ico_label)
		self.unit_info_text_label = QtWidgets.QLabel(self.unit_info)

		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setBold(False)
		font.setWeight(50)

		self.unit_info_text_label.setFont(font)
		self.unit_info_text_label.setStyleSheet("color: #FFFFFF;")
		self.unit_info_text_label.setText('Text')

		self.unit_info_layout.addWidget(self.unit_info_text_label)

		spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.unit_info_layout.addItem(spacer_item)

		self.datetime_label = QtWidgets.QLabel(self.unit_info)
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(10)
		self.datetime_label.setFont(font)
		self.datetime_label.setStyleSheet("color: #FFFFFF;")
		time_string = time.strftime('%H:%M', time.localtime())
		self.datetime_label.setText(time_string)

		self.unit_info_layout.addWidget(self.datetime_label)
		self.vertical_layout.addWidget(self.unit_info)

		self.line = QtWidgets.QFrame(self)
		self.line.setMinimumSize(QtCore.QSize(290, 3))
		self.line.setMaximumSize(QtCore.QSize(290, 3))
		self.line.setStyleSheet(
			"background-color: #EEEEEE;\n"
			"border-radius: 1px;")
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.vertical_layout.addWidget(self.line)
		self.vertical_layout.setAlignment(self.line, QtCore.Qt.AlignCenter)

		self.unit_data = QtWidgets.QWidget(self)

		self.main_text_layout = QtWidgets.QHBoxLayout(self.unit_data)
		self.main_text_layout.setContentsMargins(6, 6, 6, 6)
		self.main_text_layout.setSpacing(5)

		self.text = QtWidgets.QLabel(self.unit_data)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		self.text.setFont(font)
		self.text.setStyleSheet("color: #FFFFFF;")
		self.text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.text.setMinimumSize(QtCore.QSize(0, 104))
		# self.text.setWordWrap(True)
		self.main_text_layout.addWidget(self.text)

		self.props_layout = QtWidgets.QVBoxLayout()
		self.props_layout.setContentsMargins(9, -1, 9, -1)
		self.props_layout.setSpacing(10)

		self.application_ico = QtWidgets.QLabel(self.unit_data)
		self.application_ico.setMinimumSize(QtCore.QSize(32, 32))
		self.application_ico.setMaximumSize(QtCore.QSize(32, 32))
		self.application_ico.setText("")
		# self.application_ico.setPixmap(QtGui.QPixmap("interface/../../../../Downloads/Hnet.com-image.png"))
		self.props_layout.addWidget(self.application_ico)

		self.props_button = QtWidgets.QPushButton(self.unit_data)
		self.props_button.setMinimumSize(QtCore.QSize(32, 32))
		self.props_button.setMaximumSize(QtCore.QSize(32, 32))
		self.props_button.setStyleSheet(
			"border-radius: 8px;/*\n"
			"background-color: #4C4F57;*/\n"
			"padding: 0;\n"
			"margin: 0;\n"
			"background: transparent;")
		self.props_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("interface/../sources/images/props-ico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.props_button.setIcon(icon)
		self.props_button.setIconSize(QtCore.QSize(32, 32))
		self.props_layout.addWidget(self.props_button)

		self.main_text_layout.addLayout(self.props_layout)
		self.vertical_layout.addWidget(self.unit_data)


class StandardImageClipboardUnit(ClipboardUnit):
	"""Image clipboard unit if user copied image or make screenshot"""

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

	def update_clipboard(self) -> None:
		self._clipboard.setImage(self._image)

	def has_text(self, text: str) -> bool:
		"""image can`t has text"""
		if not text:
			return True
		return False

	def _create_widget(self) -> None:
		# TODO add function of saving image
		self._create_standard_clipboard_unit()

		# set icon
		size = QtCore.QSize(262, 160)
		pixel_map = self._pixel_map.scaled(size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.image.setPixmap(pixel_map)

	def _create_standard_clipboard_unit(self) -> None:
		self.setMinimumSize(QtCore.QSize(0, 132))
		self.setMaximumSize(QtCore.QSize(16777215, 132))
		self.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.setStyleSheet(
			"QPushButton{\n"
			"	background-color: #585B64;\n"
			"	border-radius: 5px;\n"
			"}"
			"QPushButton:hover{\n"
			"	border: 2px solid #FD7013;\n"
			"}")

		self.vertical_layout = QtWidgets.QVBoxLayout(self)
		self.vertical_layout.setContentsMargins(0, 0, 0, 0)
		self.vertical_layout.setSpacing(0)

		self.unit_info = QtWidgets.QWidget(self)
		self.unit_info.setMinimumSize(QtCore.QSize(0, 25))
		self.unit_info.setMaximumSize(QtCore.QSize(16777215, 25))
		font = QtGui.QFont()
		font.setPointSize(8)
		self.unit_info.setFont(font)

		self.unit_info_layout = QtWidgets.QHBoxLayout(self.unit_info)
		self.unit_info_layout.setContentsMargins(2, 0, 9, 0)
		self.unit_info_layout.setSpacing(0)

		self.unit_info_text_ico_label = QtWidgets.QLabel(self.unit_info)
		self.unit_info_text_ico_label.setMinimumSize(QtCore.QSize(25, 25))
		self.unit_info_text_ico_label.setMaximumSize(QtCore.QSize(25, 25))
		self.unit_info_text_ico_label.setText("")
		self.unit_info_text_ico_label.setPixmap(QtGui.QPixmap("interface/../sources/images/image-ico.svg"))

		self.unit_info_layout.addWidget(self.unit_info_text_ico_label)
		self.unit_info_text_label = QtWidgets.QLabel(self.unit_info)

		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setBold(False)
		font.setWeight(50)
		self.unit_info_text_label.setFont(font)
		self.unit_info_text_label.setStyleSheet("color: #FFFFFF;")
		self.unit_info_text_label.setText('Image')

		self.unit_info_layout.addWidget(self.unit_info_text_label)

		spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.unit_info_layout.addItem(spacer_item)

		self.datetime_label = QtWidgets.QLabel(self.unit_info)
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(10)
		self.datetime_label.setFont(font)
		self.datetime_label.setStyleSheet("color: #FFFFFF;")
		time_string = time.strftime('%H:%M', time.localtime())
		self.datetime_label.setText(time_string)

		self.unit_info_layout.addWidget(self.datetime_label)
		self.vertical_layout.addWidget(self.unit_info)

		self.line = QtWidgets.QFrame(self)
		self.line.setMinimumSize(QtCore.QSize(290, 3))
		self.line.setMaximumSize(QtCore.QSize(290, 3))
		self.line.setStyleSheet(
			"background-color: #EEEEEE;\n"
			"border-radius: 1px;")
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.vertical_layout.addWidget(self.line)
		self.vertical_layout.setAlignment(self.line, QtCore.Qt.AlignCenter)

		self.unit_data = QtWidgets.QWidget(self)

		self.main_text_layout = QtWidgets.QHBoxLayout(self.unit_data)
		self.main_text_layout.setContentsMargins(6, 6, 6, 6)
		self.main_text_layout.setSpacing(5)

		self.image = QtWidgets.QLabel(self.unit_data)
		self.image.setMinimumSize(QtCore.QSize(0, 92))
		self.image.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.image.setText("")
		self.image.setAlignment(QtCore.Qt.AlignCenter)

		self.main_text_layout.addWidget(self.image)
		self.vertical_layout.addWidget(self.unit_data)


class ImageClipboardUnit(StandardImageClipboardUnit):

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget
	):
		super(ImageClipboardUnit, self).__init__(parent, clipboard, parent_window)

	def _create_standard_clipboard_unit(self) -> None:
		StandardImageClipboardUnit._create_standard_clipboard_unit(self)

		# calculate height for image
		pixel_map_old_size = self._pixel_map.size()
		if pixel_map_old_size.height() < 260:
			pixel_map_height = pixel_map_old_size.height()
		else:
			pixel_map_height = 260

		# set minimum size of image: if image.height less than 260 -> image.height
		self.image.setMinimumSize(0, pixel_map_height)

		# set pixel map for label
		pixel_map = self._pixel_map.scaledToHeight(pixel_map_height)
		self.image.setPixmap(pixel_map)

		# calculate height of unit
		if pixel_map_height + 40 < 300:
			unit_height = pixel_map_height + 40
		else:
			unit_height = 300
		self.setFixedSize(QtCore.QSize(16777215, unit_height))


class FileClipboardUnit(ClipboardUnit):
	"""Image clipboard unit if user copied file"""

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

	def has_text(self, text: str) -> bool:
		if text.lower() in self.text.text():
			return True
		return False

	def update_clipboard(self) -> None:
		data = QtCore.QMimeData()
		urls = [QtCore.QUrl.fromLocalFile(x) for x in self._files_urls]
		data.setUrls(urls)
		self._clipboard.setMimeData(data)

	def _create_widget(self) -> None:
		file_names = [x.rsplit('/', 1)[-1] for x in self._files_urls]
		self._create_standard_clipboard_unit()
		self.text.setText('\n'.join(file_names))

	def _create_standard_clipboard_unit(self) -> None:
		self.setMinimumSize(QtCore.QSize(0, 132))
		self.setMaximumSize(QtCore.QSize(16777215, 132))
		self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.setStyleSheet(
			"QPushButton{\n"
			"	background-color: #585B64;\n"
			"	border-radius: 5px;\n"
			"}"
			"QPushButton:hover{\n"
			"	border: 2px solid #FD7013;\n"
			"}")

		self.vertical_layout = QtWidgets.QVBoxLayout(self)
		self.vertical_layout.setContentsMargins(0, 0, 0, 0)
		self.vertical_layout.setSpacing(0)

		self.unit_info = QtWidgets.QWidget(self)
		self.unit_info.setMinimumSize(QtCore.QSize(0, 25))
		self.unit_info.setMaximumSize(QtCore.QSize(16777215, 25))

		font = QtGui.QFont()
		font.setPointSize(8)
		self.unit_info.setFont(font)

		self.unit_info_layout = QtWidgets.QHBoxLayout(self.unit_info)
		self.unit_info_layout.setContentsMargins(2, 0, 9, 0)
		self.unit_info_layout.setSpacing(0)

		self.unit_info_text_ico_label = QtWidgets.QLabel(self.unit_info)
		self.unit_info_text_ico_label.setMinimumSize(QtCore.QSize(25, 25))
		self.unit_info_text_ico_label.setMaximumSize(QtCore.QSize(25, 25))
		self.unit_info_text_ico_label.setText("")
		self.unit_info_text_ico_label.setPixmap(QtGui.QPixmap("interface/../sources/images/file-ico.svg"))

		self.unit_info_layout.addWidget(self.unit_info_text_ico_label)
		self.unit_info_text_ico_label = QtWidgets.QLabel(self.unit_info)

		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setBold(False)
		font.setWeight(50)

		self.unit_info_text_ico_label.setFont(font)
		self.unit_info_text_ico_label.setStyleSheet("color: #FFFFFF;")
		self.unit_info_text_ico_label.setText('Text')

		self.unit_info_layout.addWidget(self.unit_info_text_ico_label)

		spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.unit_info_layout.addItem(spacer_item)

		self.datetime_label = QtWidgets.QLabel(self.unit_info)
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(10)
		self.datetime_label.setFont(font)
		self.datetime_label.setStyleSheet("color: #FFFFFF;")
		time_string = time.strftime('%H:%M', time.localtime())
		self.datetime_label.setText(time_string)

		self.unit_info_layout.addWidget(self.datetime_label)
		self.vertical_layout.addWidget(self.unit_info)

		self.line = QtWidgets.QFrame(self)
		self.line.setMinimumSize(QtCore.QSize(290, 3))
		self.line.setMaximumSize(QtCore.QSize(290, 3))
		self.line.setStyleSheet(
			"background-color: #EEEEEE;\n"
			"border-radius: 1px;")
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.vertical_layout.addWidget(self.line)
		self.vertical_layout.setAlignment(self.line, QtCore.Qt.AlignCenter)

		self.unit_data = QtWidgets.QWidget(self)

		self.main_text_layout = QtWidgets.QHBoxLayout(self.unit_data)
		self.main_text_layout.setContentsMargins(6, 6, 6, 6)
		self.main_text_layout.setSpacing(5)

		self.text = QtWidgets.QLabel(self.unit_data)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		self.text.setFont(font)
		self.text.setStyleSheet("color: #FFFFFF;")
		self.text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.text.setMinimumSize(QtCore.QSize(0, 104))
		self.main_text_layout.addWidget(self.text)

		self.props_layout = QtWidgets.QVBoxLayout()
		self.props_layout.setContentsMargins(9, -1, 9, -1)
		self.props_layout.setSpacing(10)

		self.open_folder_button = QtWidgets.QLabel(self.unit_data)
		self.open_folder_button.setMinimumSize(QtCore.QSize(32, 32))
		self.open_folder_button.setMaximumSize(QtCore.QSize(32, 32))
		self.open_folder_button.setText("")
		self.open_folder_button.setPixmap(QtGui.QPixmap("interface/../sources/images/folder-ico.svg"))
		self.props_layout.addWidget(self.open_folder_button)

		self.props_button = QtWidgets.QPushButton(self.unit_data)
		self.props_button.setMinimumSize(QtCore.QSize(32, 32))
		self.props_button.setMaximumSize(QtCore.QSize(32, 32))
		self.props_button.setStyleSheet(
			"border-radius: 8px;/*\n"
			"background-color: #4C4F57;*/\n"
			"padding: 0;\n"
			"margin: 0;\n"
			"background: transparent;")
		self.props_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("interface/../sources/images/props-ico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.props_button.setIcon(icon)
		self.props_button.setIconSize(QtCore.QSize(32, 32))
		self.props_layout.addWidget(self.props_button)

		self.main_text_layout.addLayout(self.props_layout)
		self.vertical_layout.addWidget(self.unit_data)


class LinkClipboardUnit(TextClipboardUnit):

	def __init__(
			self,
			parent: QtWidgets.QWidget,
			clipboard: QtGui.QClipboard,
			parent_window: QtWidgets.QWidget
	):
		super().__init__(parent, clipboard, parent_window)
		self._clipboard = clipboard

		self._text: str = self._clipboard.text()

	def _create_widget(self) -> None:
		"""normalize unit: sets standard styles, sets showing text or image"""
		self._create_standard_clipboard_unit()
		self.text.setText(self._text)

	def _create_standard_clipboard_unit(self) -> None:
		TextClipboardUnit._create_standard_clipboard_unit(self)
		self.unit_info_text_label.setText('Link')
		self.unit_info_text_ico_label.setPixmap(QtGui.QPixmap('interface/../sources/images/text-icon.svg'))
		self.application_ico.setPixmap(QtGui.QPixmap('interface/../sources/images/open-browser-ico.svg'))
		self.text.setStyleSheet('color: #0085FF;')
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setUnderline(True)
		self.text.setFont(font)


class ClipboardUnitFactory:

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

		self._clipboard.dataChanged.connect(self.create_clipboard_unit)

	def create_clipboard_unit(self) -> None:
		file_urls, image, text = self._get_data_from_clipboard()

		if text in self._data or image in self._data or file_urls in self._data:
			# if data already in clipboard, skip it
			pass
		else:
			# add unit to all_units_scrollarea_content

			if self._clipboard.mimeData().urls():
				# if we have url in urls list -> user copied file
				self._data.append(file_urls)
				self._create_clipboard_unit(self._layouts['all_units'], FileClipboardUnit)
				self._create_clipboard_unit(self._layouts['file'], FileClipboardUnit)

			elif not self._clipboard.pixmap().isNull():
				# if copied data is image
				self._data.append(image)
				self._create_clipboard_unit(self._layouts['all_units'], StandardImageClipboardUnit)
				self._create_clipboard_unit(self._layouts['image'], ImageClipboardUnit)

			elif text:
				if validators.url(text):
					# if text looks like link
					self._create_clipboard_unit(self._layouts['all_units'], LinkClipboardUnit)
					self._create_clipboard_unit(self._layouts['link'], LinkClipboardUnit)
				else:
					# just simple text
					self._create_clipboard_unit(self._layouts['all_units'], TextClipboardUnit)
					self._create_clipboard_unit(self._layouts['text'], TextClipboardUnit)

				self._data.append(text)

			else:
				raise TypeError('Now supports only text, image and files')

	def _create_clipboard_unit(self, parent: QtWidgets.QWidget, unit_class: type(ClipboardUnit)) -> None:
		"""
		:param parent:
		:param unit_class: link to class that you want to create
		:return:
		"""
		layout = parent.layout()
		unit = unit_class(parent, self._clipboard, self._parent_window)
		layout.insertWidget(0, unit)
		self._append_units_to_all_units(unit)

	def _append_units_to_all_units(self, unit: ClipboardUnit) -> None:
		self._parent_window.all_units.add(unit)

	def _get_data_from_clipboard(self) -> (list[str], QtGui.QImage, str):
		"""gets all data, that can be copied from clipboard"""
		text = self._clipboard.text()
		image = self._clipboard.image()
		file_urls = [x.path() for x in self._clipboard.mimeData().urls()]
		return file_urls, image, text

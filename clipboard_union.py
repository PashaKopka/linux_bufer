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
		self._clipboard = clipboard
		self._text = self._clipboard.text()

		# need to paste image
		self._image = self._clipboard.image() if not self._clipboard.pixmap().isNull() else None
		# need to show image in ui
		self._pixel_map = self._clipboard.pixmap() if not self._clipboard.pixmap().isNull() else None

		self._normalize_widget()
		self._parent_window = parent_window  # Need parent window to hiding it

	def _paste(self):
		"""
		paste clipboard data
		hide main window and then use shortcut <Ctrl>+C
		may be problems if is another shortcut in system for this function
		"""
		self._parent_window.hide()
		self._update_clipboard()

		keyboard_controller = keyboard.Controller()
		time.sleep(.01)  # Time to window hiding
		# TODO think about other variants
		with keyboard_controller.pressed(keyboard.Key.ctrl):
			keyboard_controller.press('v')
			keyboard_controller.release('v')

	def _update_clipboard(self):
		"""
		updates last clipboard element
		it sets data in clipboard (like you use <Ctrl>+C)
		and then you can paste this data
		"""
		if self._text:
			self._clipboard.setText(self._text)
		elif self._pixel_map:
			self._clipboard.setImage(self._image)

	def _normalize_widget(self) -> None:
		"""normalize union: sets standard styles, sets showing text or image"""
		if self._text:
			# TODO if text hasn`t \n -> text on many lines; else -> one line
			# TODO add icon of active application
			if not self._text.count('\n') or self._text.find('\n') == (len(self._text) - 1):
				label = QtWidgets.QLabel(self._text, self)
				label.setWordWrap(True)
				self._set_standard_label_styles(label)

				layout = QtWidgets.QHBoxLayout(self)
				layout.addWidget(label, 0, QtCore.Qt.AlignCenter)
			else:
				self.setText(self._text)

			self._set_standard_styles(text_align='left top')

		elif self._image:
			# TODO add function of saving image
			self._set_standard_styles(text_align='center')

			# set icon
			icon = QtGui.QIcon(self._pixel_map)
			self.setIcon(icon)
			self.setIconSize(QtCore.QSize(200, 90))

	def _set_standard_label_styles(self, label: QtWidgets.QLabel):
		label.setStyleSheet(
			'color: #fff;'
			'background-color: #414141;'
			# 'text-align:left top;'
			'padding: 0;'
		)
		size = QtCore.QSize(250, 85)
		label.setFixedSize(size)
		label.setAlignment(QtCore.Qt.AlignLeft)
		label.setAlignment(QtCore.Qt.AlignTop)

	def _set_standard_styles(self, text_align: str) -> None:
		"""
		standard looking of button of clipboard
		:param text_align: text align of the button
			for image -> center, for text -> left top
		"""
		self.setMinimumSize(QtCore.QSize(0, 100))
		self.setMaximumSize(QtCore.QSize(265, 100))
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.setStyleSheet(
			"QPushButton{\n"
			"    border: 2px solid #313131;\n"
			"    color: #fff;\n"
			"    border-radius: 10px;\n"
			"    background-color: #414141;\n"
			"    padding: 5px;\n"
			f"    text-align:{text_align};\n"
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
		self.setCheckable(True)
		self.setObjectName("pasteObject1")

import time

import pyperclip
from PyQt5 import QtWidgets, QtCore, QtGui
from pynput import keyboard


class ClipboardUnion(QtWidgets.QPushButton):

	def __init__(self, text: str, parent: QtWidgets.QWidget, parent_window: QtWidgets.QWidget):
		super().__init__(parent)
		# TODO if text hasn`t \n -> text on many lines; else -> one line
		self.setText(text)
		self._normalize_widget()
		self.clicked.connect(self._paste)

		self._text = text
		self._parent_window = parent_window  # Need parent window to hiding it

	def _paste(self):
		pyperclip.copy(self._text)
		self._parent_window.hide()

		keyboard_controller = keyboard.Controller()
		time.sleep(.01)  # Time to window hiding
		with keyboard_controller.pressed(keyboard.Key.ctrl):
			keyboard_controller.press('v')
			keyboard_controller.release('v')

	def _normalize_widget(self):
		self.setMinimumSize(QtCore.QSize(0, 100))
		self.setMaximumSize(QtCore.QSize(265, 100))
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.setStyleSheet(
			"QPushButton{\n"
			"    border: 2px solid #313131;\n"
			"    color: #fff;\n"
			"    border-radius: 10px;\n"
			"    background-color: #414141;\n"
			"    text-align:left top;\n"
			"    padding: 5px;\n"
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
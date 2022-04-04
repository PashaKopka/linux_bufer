import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton

from ui.main import Ui_Form as MainUI
from pynput import keyboard


class ShortCutFactory:

	def __init__(self, hotkey: str, function):
		"""
		:param hotkey: hotkey, that pynput supports
		:param function: link on the function, that shortcut calls
		"""
		self.hotkey = hotkey
		self.function = function
		self.activate()

	def call_function(self):
		# Send function calling to main thread
		self.function()

	def activate(self):
		def for_canonical(function):
			return lambda args: function(listener.canonical(args))

		activate_window_shortcut = keyboard.HotKey(keyboard.HotKey.parse(self.hotkey), self.call_function)
		listener = keyboard.Listener(
			on_press=for_canonical(activate_window_shortcut.press),
			on_release=for_canonical(activate_window_shortcut.release)
		)
		listener.start()


class MainWindow(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.ui = MainUI()
		self.ui.setupUi(self)

		self.shortcuts = {
			'<cmd>+v': self.show_window,
			'<ctrl>+c': self.add_buffer_union
		}

		# set window parameters
		self._setup_window()

		# activate shortcuts listening
		self._activate_shortcuts()

	def show_window(self):
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def add_buffer_union(self):
		# adding buffer union to interface
		# function calling by shortcut
		l = self.ui.scrollAreaWidgetContents.layout()
		b = QPushButton('New Button', self.ui.scrollAreaWidgetContents)
		l.addWidget(b)

	def _activate_shortcuts(self):
		# create users shortcuts
		for hotkey, function in self.shortcuts.items():
			ShortCutFactory(hotkey, function)

	def _setup_window(self):
		# setup standard window settings
		flags = Qt.FramelessWindowHint
		flags |= Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setAttribute(Qt.WA_TranslucentBackground)

	def event(self, event: QtCore.QEvent) -> bool:
		if event.type() == QtCore.QEvent.WindowDeactivate:
			self.hide()
		return super().event(event)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()

	sys.exit(app.exec())

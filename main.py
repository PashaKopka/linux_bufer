import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton

from clipboard_union import ClipboardUnion
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
		}

		# set window parameters
		self._setup_window()

		# activate shortcuts listening
		self._activate_shortcuts()

		# activate clipboard handler
		self._clipboard = QtWidgets.QApplication.clipboard()
		self._clipboard.dataChanged.connect(self.clipboard_changed)

	def show_window(self):
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def add_clipboard_union(self, clipboard_data):
		# adding buffer union to interface
		# function calling by shortcut
		layout = self.ui.scrollAreaWidgetContents.layout()
		union = ClipboardUnion(clipboard_data, self.ui.scrollAreaWidgetContents)
		layout.addWidget(union)

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

	def clipboard_changed(self):
		# Now handling only text
		# TODO handle images also
		data = self._clipboard.text()
		self.add_clipboard_union(clipboard_data=data)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()

	sys.exit(app.exec())

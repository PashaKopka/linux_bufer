import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

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

		# some variables
		self.shortcuts = {
			'<cmd>+v': self.show_window,
		}
		self._data = []

		# set window parameters
		self._setup_window()

		# activate shortcuts listening
		self._activate_shortcuts()

		# activate clipboard handler
		self._clipboard = QtWidgets.QApplication.clipboard()
		self._clipboard.dataChanged.connect(self._add_clipboard_union)

	def show_window(self):
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def _add_clipboard_union(self):
		# adding buffer union to interface
		# function calling by shortcut
		text = self._clipboard.text()
		image = self._clipboard.image()
		if text in self._data or image in self._data:
			# if data already in clipboard skip it
			pass
		else:
			layout = self.ui.scrollAreaWidgetContents.layout()
			union = ClipboardUnion(self._clipboard, self.ui.scrollAreaWidgetContents, self)
			layout.insertWidget(0, union)

			# add data to clipboard
			if text:
				self._data.append(text)
			elif not self._clipboard.pixmap().isNull():
				self._data.append(image)

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
			# when click out of window
			self.hide()
		return super().event(event)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()

	sys.exit(app.exec())

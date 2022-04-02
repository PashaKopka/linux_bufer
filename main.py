import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from ui.main import Ui_Form as MainUI
from pynput import keyboard


class MainWindow(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.ui = MainUI()
		self.ui.setupUi(self)

		# set window parameters
		self._setup_window()

		# activate shortcut listening
		self.shortcut()

	def show_window(self):
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def shortcut(self):
		def for_canonical(function):
			return lambda args: function(listener.canonical(args))

		shortcut = keyboard.HotKey(keyboard.HotKey.parse('<cmd>+v'), self.show_window)
		listener = keyboard.Listener(
			on_press=for_canonical(shortcut.press),
			on_release=for_canonical(shortcut.release)
		)
		listener.start()

	def _setup_window(self) -> None:
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
	application.show()  # TODO temp

	sys.exit(app.exec())

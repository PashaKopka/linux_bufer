import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from ui.main import Ui_Form as MainUI
from pynput import keyboard


class MainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = MainUI()
		self.ui.setupUi(self)
		self._normalize_window()

	def hotkey(self):
		def on_activate():
			self.show()
			self.activateWindow()

		def for_canonical(f):
			return lambda k: f(l.canonical(k))

		hotkey = keyboard.HotKey(
			keyboard.HotKey.parse('<cmd>+v'),
			on_activate)
		l = keyboard.Listener(
			on_press=for_canonical(hotkey.press),
			on_release=for_canonical(hotkey.release)
		)
		l.start()

	def _normalize_window(self) -> None:
		flags = Qt.FramelessWindowHint
		flags |= Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		# self.setAttribute(Qt.WA_TranslucentBackground)

	def event(self, event: QtCore.QEvent) -> bool:
		if event.type() == QtCore.QEvent.WindowDeactivate:
			self.hide()
		return super().event(event)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()
	# application.show()  # TODO temp
	application.hotkey()  # running shortcut handling

	sys.exit(app.exec())

import sys

import validators as validators
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
		"""
		calls function of shortcut
		may be some decorators
		"""
		self.function()

	def activate(self):
		"""
		activate shortcut listener
		"""
		def for_canonical(function):
			return lambda args: function(listener.canonical(args))

		# set hotkey
		activate_window_shortcut = keyboard.HotKey(keyboard.HotKey.parse(self.hotkey), self.call_function)

		# create listener and start listening
		listener = keyboard.Listener(
			on_press=for_canonical(activate_window_shortcut.press),
			on_release=for_canonical(activate_window_shortcut.release)
		)
		listener.start()


class MainWindow(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		# set UI
		self.ui = MainUI()
		self.ui.setupUi(self)

		# create some variables
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
		"""
		function of window showing
		if you want to make window.show() use this function
		"""
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def _add_clipboard_union(self):
		"""
		adding clipboard union to interface and data to self._data
		function calling if clipboard update
		"""
		text = self._clipboard.text()
		image = self._clipboard.image()

		if text in self._data or image in self._data:
			# if data already in clipboard skip it
			pass
		else:
			# add union to all_unions_scrollarea_content
			self._add_clipboard_union_to_layout(self.ui.all_unions_scrollarea_content)

			# TODO may be do something better
			# add data to clipboard
			if text:
				if validators.url(text):
					self._add_clipboard_union_to_layout(self.ui.links_scrollarea_content)
				else:
					self._add_clipboard_union_to_layout(self.ui.text_scrollarea_content)

				self._data.append(text)
			elif not self._clipboard.pixmap().isNull():
				self._data.append(image)
				self._add_clipboard_union_to_layout(self.ui.images_scrollarea_content)

	def _add_clipboard_union_to_layout(self, _layout):
		layout = _layout.layout()
		union = ClipboardUnion(self._clipboard, _layout, self)
		layout.insertWidget(0, union)

	def _activate_shortcuts(self):
		"""
		create and activate users shortcuts listeners
		"""
		for hotkey, function in self.shortcuts.items():
			ShortCutFactory(hotkey, function)

	def _setup_window(self):
		"""
		setup standard main window settings
		"""
		flags = Qt.FramelessWindowHint
		flags |= Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setAttribute(Qt.WA_TranslucentBackground)

	def event(self, event: QtCore.QEvent) -> bool:
		"""
		override event handler
		"""
		if event.type() == QtCore.QEvent.WindowDeactivate:
			# when click out of window
			self.hide()
		return super().event(event)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()

	sys.exit(app.exec())

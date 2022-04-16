import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from clipboard_union import ClipboardUnionFactory
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
		self.all_unions: set[QtWidgets.QPushButton] = set()

		# set window parameters
		self._setup_window()

		# activate shortcuts listening
		self._activate_shortcuts()

		# layouts links
		self._layouts = {
			'all_unions': self.ui.all_unions_scrollarea_content,
			'text': self.ui.text_scrollarea_content,
			'image': self.ui.images_scrollarea_content,
			'file': self.ui.files_scrollarea_content,
			'link': self.ui.links_scrollarea_content
		}
		# activate clipboard handler and clipboard unions factory
		self._clipboard = QtWidgets.QApplication.clipboard()
		self._clipboard_union_factory = ClipboardUnionFactory(
			self._clipboard,
			parent_window=self,
			layouts=self._layouts
		)

		# activate search
		self.ui.searchbar.textChanged.connect(self._search_unions)

	def show_window(self):
		"""
		function of window showing
		if you want to make window.show() use this function
		"""
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def hide_window(self):
		self.hide()

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

	def _search_unions(self, text):
		for widget in self.all_unions:
			if self.text_in_widget(widget, text):
				widget.show()
			else:
				widget.hide()

	def event(self, event: QtCore.QEvent) -> bool:
		"""
		override event handler
		"""
		if event.type() == QtCore.QEvent.WindowDeactivate:
			# when click out of window
			self.hide()
		elif event.type() == QtCore.QEvent.Hide:
			self.event(QtCore.QEvent(QtCore.QEvent.WindowDeactivate))
		return super().event(event)

	@staticmethod
	def text_in_widget(widget: QtWidgets.QPushButton, text: str) -> bool:
		try:
			widget_text = widget.children()[0].text().lower()
		except IndexError:
			widget_text = widget.text()

		if text.lower() in widget_text:
			return True
		return False


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()

	sys.exit(app.exec())

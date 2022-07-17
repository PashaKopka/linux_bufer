import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from clipboard_unit import ClipboardUnitFactory, ClipboardUnit
from config import ACTIVATE_HOTKEY
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
			ACTIVATE_HOTKEY: self.show_window,
		}
		self.all_units: set[ClipboardUnit] = set()
		self._hide_window = True
		self._window_active = True
		self.mouse_in = False  # if mouse over the main window -> mouse_in == True
		# TODO This is crutch, maybe change it letter

		# set window parameters
		self._setup_window()

		# activate shortcuts listening
		self._activate_shortcuts()

		# layouts links
		self._layouts = {
			'all_units': self.ui.all_units_scrollarea_content,
			'text': self.ui.text_units_scrollarea_content,
			'image': self.ui.images_units_scrollarea_content,
			'file': self.ui.files_units_scrollarea_content,
			'link': self.ui.links_units_scrollarea_content
		}
		# activate clipboard handler and clipboard units factory
		self._clipboard = QtWidgets.QApplication.clipboard()
		self._clipboard_unit_factory = ClipboardUnitFactory(
			self._clipboard,
			parent_window=self,
			layouts=self._layouts
		)

		# activate search
		self.ui.searchbar.textChanged.connect(self._search_units)

	def show_window(self) -> None:
		"""
		function of window showing
		if you want to make window.show() use this function
		"""
		position = QCursor.pos()
		self.move(position)
		self.show()
		self.activateWindow()

	def hide_window(self) -> None:
		for unit in self.all_units:
			unit.hide_details_window()
		self.hide()

	def dont_hide_window_this_time(self):
		self._hide_window = False

	def activate_window(self):
		self._window_active = True

	def deactivate_window(self):
		self._window_active = False

	def is_window_active(self):
		return self._window_active

	def _activate_shortcuts(self) -> None:
		"""
		create and activate users shortcuts listeners
		"""
		for hotkey, function in self.shortcuts.items():
			ShortCutFactory(hotkey, function)

	def _setup_window(self) -> None:
		"""
		setup standard main window settings
		"""
		# general window settings
		flags = Qt.FramelessWindowHint
		# flags |= Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setAttribute(Qt.WA_TranslucentBackground)

		# set shadow effect for tabs
		# TODO extract method
		grey_shadow_effect = QtWidgets.QGraphicsDropShadowEffect()
		grey_shadow_effect.setBlurRadius(7)
		grey_shadow_effect.setColor(QtGui.QColor(88, 91, 100, 120))
		grey_shadow_effect.setXOffset(0)
		grey_shadow_effect.setYOffset(4)
		self.ui.tabWidget.tabBar().setGraphicsEffect(grey_shadow_effect)

	def _search_units(self, text: str) -> None:
		"""
		function for searching units
		just show widget if it has text, that user typed in self.ui.searchbar
		"""
		for unit in self.all_units:
			if unit.has_text(text):
				unit.show()
			else:
				unit.hide()

	def event(self, event: QtCore.QEvent) -> bool:
		"""
		override event handler
		"""
		if event.type() == QtCore.QEvent.WindowDeactivate:
			# when click outside of window
			# if you want to not hide window once you can call dont_hide_window_this_time method
			# then _hide_window becomes False and window will not hide once
			if self._hide_window:
				self.hide_window()
			else:
				self._hide_window = True
		return super().event(event)

	def enterEvent(self, a0: QtCore.QEvent) -> None:
		self.mouse_in = True

	def leaveEvent(self, a0: QtCore.QEvent) -> None:
		self.mouse_in = False


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	application = MainWindow()

	sys.exit(app.exec())

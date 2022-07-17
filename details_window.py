from PyQt5.QtCore import Qt

from ui.details_window import Ui_Frame as DetailsUi
from PyQt5 import QtWidgets, QtCore


class DetailsWindow(QtWidgets.QWidget):
	"""Details window, user can show all data, that was copied"""

	def __init__(self, clipboard_unit, parent_window: QtWidgets.QWidget):
		super().__init__()
		# set UI
		self.ui = DetailsUi()
		self.ui.setupUi(self)
		self._parent_window = parent_window
		self._clipboard_unit = clipboard_unit

		self.setup_window()

	def setup_window(self):
		flags = QtCore.Qt.FramelessWindowHint
		flags |= QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.ui.content.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

	def show_window(self):
		"""custom method of show, should to use it"""
		if self._clipboard_unit.is_texted_unit():
			self.ui.content.setText(self._clipboard_unit.get_text())
		else:
			pixmap = self._clipboard_unit.get_pixel_map()
			pixmap = pixmap.scaledToWidth(400)
			self.ui.content.setPixmap(pixmap)
		self.show()

	def hide_window(self):
		# custom method of hiding window, should to use it
		self.hide()

	def event(self, event: QtCore.QEvent) -> bool:
		"""
		override event handler
		"""
		if event.type() == QtCore.QEvent.WindowDeactivate:
			self.hide_window()
			# hiding also parent_window when pressing outside
			if not self._parent_window.mouse_in:
				self._parent_window.hide_window()
			else:
				self._parent_window.deactivate_window()
		return super().event(event)

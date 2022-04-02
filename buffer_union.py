from PyQt5 import QtWidgets, QtCore, QtGui


class BufferUnionUi(QtWidgets.QPushButton):

	def __init__(self, text: str, parent: QtWidgets.QWidget):
		super().__init__(parent)
		self.setText(text)
		self._normalize_widget()
		# self.moveToThread(parent)

	def _normalize_widget(self):
		self.setMinimumSize(QtCore.QSize(0, 60))
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.setStyleSheet(
			"QPushButton{\n"
			"    border: 2px solid #313131;\n"
			"    color: #fff;\n"
			"    border-radius: 10px;\n"
			"    background-color: #414141;\n"
			"    text-align:left;\n"
			"    padding: 5px;\n"
			"    vertical-align: text-top;\n"
			"}\n"
			"\n"
			"QPushButton:hover{\n"
			"    border: 2px solid #08ffc8;\n"
			"}\n"
			"\n"
			"QPushButton:pressed{\n"
			"    background-color: #313131;\n"
			"    border: 2px solid #08ffc8;\n"
			"}")
		self.setCheckable(True)
		self.setObjectName("pasteObject1")

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/details_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(425, 315)
        Frame.setMinimumSize(QtCore.QSize(425, 315))
        Frame.setMaximumSize(QtCore.QSize(425, 315))
        Frame.setStyleSheet("background-color: #585B64;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Frame)
        self.scrollArea.setStyleSheet("QScrollArea {\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 6px;\n"
"    margin: 6px 0 6px 0;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 6px;\n"
"    margin: 0 6px 0 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: #a39e9e;\n"
"    border-radius: 3px;\n"
"    min-height: 30px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"    background-color: #a39e9e;\n"
"    border-radius: 3px;\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1499, 918))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(7, 7, 7, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.content.setFont(font)
        self.content.setStyleSheet("color: #FFF;")
        self.content.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.content.setObjectName("content")
        self.verticalLayout_2.addWidget(self.content)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.content.setText(_translate("Frame", "<html><head/><body><p>TextLabel</p><p>TextLabel</p><p>TextLabel</p><p>TextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabelTextLabel</p><p><br/></p><p>TextLabel</p><p>TextLabelv</p><p><br/></p><p>v</p><p>v</p><p>TextLabel</p><p>TextLabel</p><p>vvTextLabelvTextLabel</p><p>TextLabelTextLabelv</p><p><br/></p><p>TextLabel</p><p>TextLabel</p><p>TextLabel</p><p>TextLabel</p><p>v</p><p>TextLabel</p><p>TextLabel</p><p>TextLabel</p><p>TextLabelTextLabel</p><p>TextLabel</p><p>TextLabelTextLabel</p></body></html>"))

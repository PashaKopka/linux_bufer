# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        Form.setMinimumSize(QtCore.QSize(300, 400))
        Form.setMaximumSize(QtCore.QSize(300, 400))
        Form.setStyleSheet("border: 1px solid #FFF;\n"
"border-radius: 30px;\n"
"background-color: #525252;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: #525252;\n"
"border: 2 px solid #000;\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: 2px solid #313131;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"    background-color: #414141;\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid #313131;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"    background-color: #414141;\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("/* Vertical */\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background-color: #313131;\n"
"    width: 10px;\n"
"    margin: 11px 0 11px 0; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: #a39e9e;\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color: #EAEAEA;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    width: 0;\n"
"    height: 0;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 290, 338))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pasteObject1_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pasteObject1_16.setMinimumSize(QtCore.QSize(0, 100))
        self.pasteObject1_16.setMaximumSize(QtCore.QSize(265, 100))
        self.pasteObject1_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pasteObject1_16.setAccessibleDescription("")
        self.pasteObject1_16.setStyleSheet("QPushButton{\n"
"    border: 2px solid #313131;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"    background-color: #414141;\n"
"    text-align:left top;\n"
"    padding: 5px;\n"
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
        self.pasteObject1_16.setCheckable(True)
        self.pasteObject1_16.setObjectName("pasteObject1_16")
        self.verticalLayout_2.addWidget(self.pasteObject1_16)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        self.pasteObject1_16.clicked.connect(Form.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.scrollArea, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pasteObject1_16)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pasteObject1_16.setText(_translate("Form", "123\n"
"\n"
"\\n\n"
"\n"
"\n"
"\n"
"naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
"aaa\n"
"\n"
"\n"
"aaaaaaaaaaaaaaaaaaaaaaaa"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/new_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 500)
        Form.setMinimumSize(QtCore.QSize(320, 500))
        Form.setMaximumSize(QtCore.QSize(320, 16777215))
        Form.setStyleSheet(".main_form{\n"
"    padding: 10px;\n"
"    width: 320px;\n"
"    height: 500px;\n"
"    background: #C4C4C4;\n"
"    border-radius: 50px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet(".frame{\n"
"    background-color: #C4C4C4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchbar = QtWidgets.QLineEdit(self.frame)
        self.searchbar.setMinimumSize(QtCore.QSize(230, 32))
        self.searchbar.setMaximumSize(QtCore.QSize(230, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.searchbar.setFont(font)
        self.searchbar.setStyleSheet("padding: 4px 2px 4px 30px;\n"
"background-color: #F4F4F4;\n"
"border-radius: 5px;\n"
"margin: 0px;\n"
"background-image: url(\'/home/pasha/coding/python/linux_bufer/sources/images/search.svg\'); /* actual size, e.g. 16x16 */\n"
"background-repeat: no-repeat;")
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_2.addWidget(self.searchbar)
        self.verticalLayout_17.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    border: 2px solid #585B64;\n"
"    color: #fff;\n"
"    border-radius: 13px;\n"
"    background-color: #585B64;\n"
"    padding: 3px 15px;\n"
"    margin: 5px 2.5px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    border: 2px solid #FD7013;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #FD7013;\n"
"    border: 2px solid #FD7013;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 0;\n"
"    padding: 0;\n"
"    margin-top: 5px;\n"
"}\n"
"\n"
".scrollarea_content {\n"
"    background-color: #C4C4C4;\n"
"}\n"
"\n"
"/* SCROLLAREA */\n"
"\n"
"QScrollArea {\n"
"    background-color: #C4C4C4;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: transparent;\n"
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
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.all_tab = QtWidgets.QWidget()
        self.all_tab.setObjectName("all_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.all_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.all_tab)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.all_units_scrollarea_content = QtWidgets.QWidget()
        self.all_units_scrollarea_content.setGeometry(QtCore.QRect(0, 0, 308, 543))
        self.all_units_scrollarea_content.setObjectName("all_units_scrollarea_content")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.all_units_scrollarea_content)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.text_unit = QtWidgets.QWidget(self.all_units_scrollarea_content)
        self.text_unit.setMinimumSize(QtCore.QSize(0, 132))
        self.text_unit.setMaximumSize(QtCore.QSize(16777215, 132))
        self.text_unit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.text_unit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_unit.setStyleSheet(".clipboard_union{\n"
"    background-color: #585B64;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".clipboard_union:hover{\n"
"    border: 2px solid #FD7013;\n"
"}")
        self.text_unit.setObjectName("text_unit")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.text_unit)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.unit_info = QtWidgets.QWidget(self.text_unit)
        self.unit_info.setMinimumSize(QtCore.QSize(0, 25))
        self.unit_info.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.unit_info.setFont(font)
        self.unit_info.setObjectName("unit_info")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.unit_info)
        self.horizontalLayout.setContentsMargins(0, 0, 7, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.unit_info)
        self.label_3.setMinimumSize(QtCore.QSize(25, 25))
        self.label_3.setMaximumSize(QtCore.QSize(25, 25))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("interface/../sources/images/text-icon.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.unit_info)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFFFFF;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.unit_info)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFFFFF;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_8.addWidget(self.unit_info)
        self.line = QtWidgets.QFrame(self.text_unit)
        self.line.setMinimumSize(QtCore.QSize(290, 3))
        self.line.setMaximumSize(QtCore.QSize(290, 3))
        self.line.setStyleSheet("background-color: #EEEEEE;\n"
"border-radius: 1px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.unit_data = QtWidgets.QWidget(self.text_unit)
        self.unit_data.setObjectName("unit_data")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.unit_data)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.text = QtWidgets.QLabel(self.unit_data)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setStyleSheet("color: #FFFFFF;")
        self.text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setObjectName("text")
        self.horizontalLayout_3.addWidget(self.text)
        self.props = QtWidgets.QVBoxLayout()
        self.props.setContentsMargins(9, -1, 9, -1)
        self.props.setSpacing(10)
        self.props.setObjectName("props")
        self.label_4 = QtWidgets.QLabel(self.unit_data)
        self.label_4.setMinimumSize(QtCore.QSize(32, 32))
        self.label_4.setMaximumSize(QtCore.QSize(32, 32))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("interface/../../../../Downloads/Hnet.com-image.png"))
        self.label_4.setObjectName("label_4")
        self.props.addWidget(self.label_4)
        self.props_button = QtWidgets.QPushButton(self.unit_data)
        self.props_button.setMinimumSize(QtCore.QSize(32, 32))
        self.props_button.setMaximumSize(QtCore.QSize(32, 32))
        self.props_button.setStyleSheet("border-radius: 8px;/*\n"
"background-color: #4C4F57;*/\n"
"padding: 0;\n"
"margin: 0;\n"
"background: transparent;")
        self.props_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/../sources/images/props-ico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.props_button.setIcon(icon)
        self.props_button.setIconSize(QtCore.QSize(32, 32))
        self.props_button.setObjectName("props_button")
        self.props.addWidget(self.props_button)
        self.horizontalLayout_3.addLayout(self.props)
        self.verticalLayout_8.addWidget(self.unit_data)
        self.verticalLayout_10.addWidget(self.text_unit)
        self.files_unit = QtWidgets.QWidget(self.all_units_scrollarea_content)
        self.files_unit.setMinimumSize(QtCore.QSize(0, 132))
        self.files_unit.setMaximumSize(QtCore.QSize(16777215, 132))
        self.files_unit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.files_unit.setStyleSheet(".clipboard_union{\n"
"    background-color: #585B64;\n"
"    border-radius: 5px;\n"
"}")
        self.files_unit.setObjectName("files_unit")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.files_unit)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.unit_info_2 = QtWidgets.QWidget(self.files_unit)
        self.unit_info_2.setMinimumSize(QtCore.QSize(0, 25))
        self.unit_info_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.unit_info_2.setFont(font)
        self.unit_info_2.setObjectName("unit_info_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.unit_info_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 7, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.unit_info_2)
        self.label_5.setMinimumSize(QtCore.QSize(25, 25))
        self.label_5.setMaximumSize(QtCore.QSize(25, 25))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("interface/../sources/images/file-ico.svg"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.unit_info_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #FFFFFF;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.unit_info_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #FFFFFF;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout_9.addWidget(self.unit_info_2)
        self.line_2 = QtWidgets.QFrame(self.files_unit)
        self.line_2.setMinimumSize(QtCore.QSize(290, 3))
        self.line_2.setMaximumSize(QtCore.QSize(290, 3))
        self.line_2.setStyleSheet("background-color: #EEEEEE;\n"
"border-radius: 1px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_9.addWidget(self.line_2)
        self.unit_data_2 = QtWidgets.QWidget(self.files_unit)
        self.unit_data_2.setObjectName("unit_data_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.unit_data_2)
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.text_2 = QtWidgets.QLabel(self.unit_data_2)
        self.text_2.setMinimumSize(QtCore.QSize(233, 0))
        self.text_2.setMaximumSize(QtCore.QSize(233, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color: #FFFFFF;")
        self.text_2.setText("")
        self.text_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text_2.setWordWrap(True)
        self.text_2.setObjectName("text_2")
        self.horizontalLayout_5.addWidget(self.text_2)
        self.props_2 = QtWidgets.QVBoxLayout()
        self.props_2.setContentsMargins(9, -1, 9, -1)
        self.props_2.setSpacing(10)
        self.props_2.setObjectName("props_2")
        self.label_8 = QtWidgets.QLabel(self.unit_data_2)
        self.label_8.setMinimumSize(QtCore.QSize(32, 32))
        self.label_8.setMaximumSize(QtCore.QSize(32, 32))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("interface/../sources/images/folder-ico.svg"))
        self.label_8.setObjectName("label_8")
        self.props_2.addWidget(self.label_8)
        self.props_button_2 = QtWidgets.QPushButton(self.unit_data_2)
        self.props_button_2.setMinimumSize(QtCore.QSize(32, 32))
        self.props_button_2.setMaximumSize(QtCore.QSize(32, 32))
        self.props_button_2.setStyleSheet("border-radius: 8px;\n"
"background-color: #4C4F57;\n"
"padding: 0;\n"
"margin: 0;")
        self.props_button_2.setText("")
        self.props_button_2.setIcon(icon)
        self.props_button_2.setIconSize(QtCore.QSize(32, 32))
        self.props_button_2.setObjectName("props_button_2")
        self.props_2.addWidget(self.props_button_2)
        self.horizontalLayout_5.addLayout(self.props_2)
        self.verticalLayout_9.addWidget(self.unit_data_2)
        self.verticalLayout_10.addWidget(self.files_unit)
        self.image_unit_3 = QtWidgets.QWidget(self.all_units_scrollarea_content)
        self.image_unit_3.setMinimumSize(QtCore.QSize(0, 132))
        self.image_unit_3.setMaximumSize(QtCore.QSize(16777215, 132))
        self.image_unit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_unit_3.setStyleSheet(".clipboard_union{\n"
"    background-color: #585B64;\n"
"    border-radius: 5px;\n"
"}")
        self.image_unit_3.setObjectName("image_unit_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.image_unit_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.unit_info_6 = QtWidgets.QWidget(self.image_unit_3)
        self.unit_info_6.setMinimumSize(QtCore.QSize(0, 25))
        self.unit_info_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.unit_info_6.setFont(font)
        self.unit_info_6.setObjectName("unit_info_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.unit_info_6)
        self.horizontalLayout_12.setContentsMargins(0, 0, 7, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_18 = QtWidgets.QLabel(self.unit_info_6)
        self.label_18.setMinimumSize(QtCore.QSize(25, 25))
        self.label_18.setMaximumSize(QtCore.QSize(25, 25))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("interface/../sources/images/image-ico.svg"))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_12.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.unit_info_6)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: #FFFFFF;")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.label_20 = QtWidgets.QLabel(self.unit_info_6)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: #FFFFFF;")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_12.addWidget(self.label_20)
        self.verticalLayout_13.addWidget(self.unit_info_6)
        self.line_6 = QtWidgets.QFrame(self.image_unit_3)
        self.line_6.setMinimumSize(QtCore.QSize(290, 3))
        self.line_6.setMaximumSize(QtCore.QSize(290, 3))
        self.line_6.setStyleSheet("background-color: #EEEEEE;\n"
"border-radius: 1px;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_13.addWidget(self.line_6)
        self.unit_data_6 = QtWidgets.QWidget(self.image_unit_3)
        self.unit_data_6.setObjectName("unit_data_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.unit_data_6)
        self.horizontalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.text_6 = QtWidgets.QLabel(self.unit_data_6)
        self.text_6.setMinimumSize(QtCore.QSize(0, 0))
        self.text_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("color: #FFFFFF;")
        self.text_6.setText("")
        self.text_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text_6.setWordWrap(True)
        self.text_6.setObjectName("text_6")
        self.horizontalLayout_13.addWidget(self.text_6)
        self.verticalLayout_13.addWidget(self.unit_data_6)
        self.verticalLayout_10.addWidget(self.image_unit_3)
        self.image_unit_2 = QtWidgets.QWidget(self.all_units_scrollarea_content)
        self.image_unit_2.setMinimumSize(QtCore.QSize(0, 132))
        self.image_unit_2.setMaximumSize(QtCore.QSize(16777215, 132))
        self.image_unit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_unit_2.setStyleSheet(".clipboard_union{\n"
"    background-color: #585B64;\n"
"    border-radius: 5px;\n"
"}")
        self.image_unit_2.setObjectName("image_unit_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.image_unit_2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.unit_info_5 = QtWidgets.QWidget(self.image_unit_2)
        self.unit_info_5.setMinimumSize(QtCore.QSize(0, 25))
        self.unit_info_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.unit_info_5.setFont(font)
        self.unit_info_5.setObjectName("unit_info_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.unit_info_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 7, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.unit_info_5)
        self.label_15.setMinimumSize(QtCore.QSize(25, 25))
        self.label_15.setMaximumSize(QtCore.QSize(25, 25))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("interface/../sources/images/image-ico.svg"))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.unit_info_5)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #FFFFFF;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.label_17 = QtWidgets.QLabel(self.unit_info_5)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: #FFFFFF;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.verticalLayout_12.addWidget(self.unit_info_5)
        self.line_5 = QtWidgets.QFrame(self.image_unit_2)
        self.line_5.setMinimumSize(QtCore.QSize(290, 3))
        self.line_5.setMaximumSize(QtCore.QSize(290, 3))
        self.line_5.setStyleSheet("background-color: #EEEEEE;\n"
"border-radius: 1px;")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_12.addWidget(self.line_5)
        self.unit_data_5 = QtWidgets.QWidget(self.image_unit_2)
        self.unit_data_5.setObjectName("unit_data_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.unit_data_5)
        self.horizontalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.text_5 = QtWidgets.QLabel(self.unit_data_5)
        self.text_5.setMinimumSize(QtCore.QSize(0, 0))
        self.text_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color: #FFFFFF;")
        self.text_5.setText("")
        self.text_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text_5.setWordWrap(True)
        self.text_5.setObjectName("text_5")
        self.horizontalLayout_11.addWidget(self.text_5)
        self.verticalLayout_12.addWidget(self.unit_data_5)
        self.verticalLayout_10.addWidget(self.image_unit_2)
        self.scrollArea.setWidget(self.all_units_scrollarea_content)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.all_tab, "")
        self.text_tab = QtWidgets.QWidget()
        self.text_tab.setObjectName("text_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.text_tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.text_tab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.text_units_scrollarea_content = QtWidgets.QWidget()
        self.text_units_scrollarea_content.setGeometry(QtCore.QRect(0, 0, 308, 407))
        self.text_units_scrollarea_content.setObjectName("text_units_scrollarea_content")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.text_units_scrollarea_content)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(20, 386, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem4)
        self.scrollArea_2.setWidget(self.text_units_scrollarea_content)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.text_tab, "")
        self.images_tab = QtWidgets.QWidget()
        self.images_tab.setObjectName("images_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.images_tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.images_tab)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.images_units_scrollarea_content = QtWidgets.QWidget()
        self.images_units_scrollarea_content.setGeometry(QtCore.QRect(0, 0, 308, 407))
        self.images_units_scrollarea_content.setObjectName("images_units_scrollarea_content")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.images_units_scrollarea_content)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem5 = QtWidgets.QSpacerItem(20, 386, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem5)
        self.scrollArea_3.setWidget(self.images_units_scrollarea_content)
        self.verticalLayout_5.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.images_tab, "")
        self.files_tab = QtWidgets.QWidget()
        self.files_tab.setObjectName("files_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.files_tab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.files_tab)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.files_units_scrollarea_content = QtWidgets.QWidget()
        self.files_units_scrollarea_content.setGeometry(QtCore.QRect(0, 0, 308, 407))
        self.files_units_scrollarea_content.setObjectName("files_units_scrollarea_content")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.files_units_scrollarea_content)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem6 = QtWidgets.QSpacerItem(20, 386, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem6)
        self.scrollArea_4.setWidget(self.files_units_scrollarea_content)
        self.verticalLayout_6.addWidget(self.scrollArea_4)
        self.tabWidget.addTab(self.files_tab, "")
        self.links_tab = QtWidgets.QWidget()
        self.links_tab.setObjectName("links_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.links_tab)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.links_tab)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.links_units_scrollarea_content = QtWidgets.QWidget()
        self.links_units_scrollarea_content.setGeometry(QtCore.QRect(0, 0, 308, 407))
        self.links_units_scrollarea_content.setObjectName("links_units_scrollarea_content")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.links_units_scrollarea_content)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        spacerItem7 = QtWidgets.QSpacerItem(20, 386, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem7)
        self.scrollArea_5.setWidget(self.links_units_scrollarea_content)
        self.verticalLayout_7.addWidget(self.scrollArea_5)
        self.tabWidget.addTab(self.links_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_17.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setProperty("class", _translate("Form", "main_form"))
        self.frame.setProperty("class", _translate("Form", "frame"))
        self.searchbar.setPlaceholderText(_translate("Form", "Type to search..."))
        self.all_units_scrollarea_content.setProperty("class", _translate("Form", "scrollarea_content"))
        self.text_unit.setProperty("class", _translate("Form", "clipboard_union"))
        self.label.setText(_translate("Form", "Text"))
        self.label_2.setText(_translate("Form", "10.07.03"))
        self.text.setText(_translate("Form", "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut\n"
"ut\n"
"1"))
        self.files_unit.setProperty("class", _translate("Form", "clipboard_union"))
        self.label_6.setText(_translate("Form", "Files"))
        self.label_7.setText(_translate("Form", "10.07.03"))
        self.image_unit_3.setProperty("class", _translate("Form", "clipboard_union"))
        self.label_19.setText(_translate("Form", "Image"))
        self.label_20.setText(_translate("Form", "10.07.03"))
        self.image_unit_2.setProperty("class", _translate("Form", "clipboard_union"))
        self.label_16.setText(_translate("Form", "Image"))
        self.label_17.setText(_translate("Form", "10.07.03"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all_tab), _translate("Form", "All"))
        self.text_units_scrollarea_content.setProperty("class", _translate("Form", "scrollarea_content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.text_tab), _translate("Form", "Text"))
        self.images_units_scrollarea_content.setProperty("class", _translate("Form", "scrollarea_content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.images_tab), _translate("Form", "Images"))
        self.files_units_scrollarea_content.setProperty("class", _translate("Form", "scrollarea_content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.files_tab), _translate("Form", "Files"))
        self.links_units_scrollarea_content.setProperty("class", _translate("Form", "scrollarea_content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.links_tab), _translate("Form", "Links"))

# Form implementation generated from reading ui file 'notif.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class NotificationWidget(object):
    def __init__(self, title):
        self.title = title

    def setupUi(self, notif):
        notif.setObjectName("notif")
        notif.resize(900, 600)
        notif.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        notif.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        notif.setMinimumSize(QtCore.QSize(900, 600))
        notif.setMaximumSize(QtCore.QSize(900, 600))
        notif.setWindowTitle("")
        self.widget = QtWidgets.QWidget(parent=notif)
        self.widget.setGeometry(QtCore.QRect(25, 25, 850, 550))
        self.widget.setMinimumSize(QtCore.QSize(850, 550))
        self.widget.setMaximumSize(QtCore.QSize(850, 550))
        self.widget.setObjectName("widget")
        self.mainFrame = QtWidgets.QFrame(parent=self.widget)
        self.mainFrame.setGeometry(QtCore.QRect(25, 25, 800, 500))
        self.mainFrame.setMinimumSize(QtCore.QSize(800, 500))
        self.mainFrame.setMaximumSize(QtCore.QSize(800, 500))
        self.mainFrame.setStyleSheet("#mainFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.51118, y1:0.346, x2:0.538596, y2:1, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));border-radius: 24px;\n"
"}\n"
"QLabel {\n"
"color: rgb(0, 29, 61);\n"
"font-weight:bold;\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.mainFrame.setLineWidth(0)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(parent=self.mainFrame)
        self.title.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title.setObjectName("title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.title)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.notif_title = QtWidgets.QLabel(parent=self.title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.notif_title.setFont(font)
        self.notif_title.setLineWidth(0)
        self.notif_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.notif_title.setWordWrap(False)
        self.notif_title.setObjectName("notif_title")
        self.verticalLayout_3.addWidget(self.notif_title, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addWidget(self.title)
        self.content = QtWidgets.QFrame(parent=self.mainFrame)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.notif_content = QtWidgets.QLabel(parent=self.content)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.notif_content.setFont(font)
        self.notif_content.setLineWidth(0)
        self.notif_content.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.notif_content.setWordWrap(False)
        self.notif_content.setObjectName("notif_content")
        self.verticalLayout_2.addWidget(self.notif_content, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addWidget(self.content)

        self.retranslateUi(notif)
        QtCore.QMetaObject.connectSlotsByName(notif)

    def retranslateUi(self, notif):
        _translate = QtCore.QCoreApplication.translate
        self.notif_title.setText(_translate("notif", self.title))
        self.notif_content.setText(_translate("notif", "get ready to take a shot ..."))

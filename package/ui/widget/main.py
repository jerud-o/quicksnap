import pyautogui
from functools import partial
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import package.resource.resources_rc
from main import resource_path
from package.thread.video import VideoThread
from package.module.countdown_timer import CountdownTimerModule
from package.module.print import PrintModule
from package.ui.widget.notification import NotificationWidget
from package.ui.widget.popup import PopupWidget
from package.ui.widget.quicksnap import QuickSnapWidget # error: Dot between widget and quicksnap was removed


# class MainWidget(): wrong\\\\\\\\\\
class MainWidget(object):
    def __init__(self, MainWindow):
        self.width, self.height = pyautogui.size()
        self.capture_method_value = 0
        self.print_method_value = -1
        #self.gender_value = wrong
        self.gender_value = -1
        self.frame_to_print = None

        self.__init_modules()
        self.__init_ui(MainWindow)
        
        self.retranslate_ui(MainWindow)
        #self.stackedWidget.setCurrentIndex(O) wrong
        self.stackedWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def __init_modules(self):
        self.video_thread = VideoThread()
        self.countdown_module = CountdownTimerModule()
        self.print_module = PrintModule()

    #def __init_ui(self,): wrong
    def __init_ui(self, MainWindow):
        self.__init_main_window(MainWindow)
        self.__init_intro_page()
        self.__init_capture_method_page()
        self.__init_gender_selection_page()
        self.__init_formal_capture_page()
        self.__init_beauty_capture_page()
        self.__init_capture_preview_page()
        self.__init_package_selection_page()
        self.__init_printing_page()
        self.__init_get_photo_page()
        self.__init_alert_page()
        self.__init_slots()
    
    def __init_main_window(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.resize(self.width, self.height)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\quicksnap.ico")),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("padding: 0px;\n"
                                 "margin: 0px;\n"
                                 "height: 100%;\n"
                                 "width: 100%;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet("padding: 0px;\n"
                                         "margin: 0px;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.mainFrame.setLineWidth(0)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.mainFrame)
        self.stackedWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        MainWindow.setCentralWidget(self.centralwidget)

    # index 0: Landing Page (Veloria)
    def __init_intro_page(self):
        # Widget for the whole page
        self.intro = QtWidgets.QWidget()
        self.intro.setStyleSheet("")
        self.intro.setObjectName("intro")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.intro)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        # Frame with orange cirles and blue background
        self.intro_frame = QtWidgets.QFrame(parent=self.intro)
        self.intro_frame.setStyleSheet("#intro_frame {\n"
                                       "border-image: url('" + resource_path("package\\resource\\img\\intro_bg.png").replace("\\", "/") + "') 0 0 0 0 stretch stretch;\n"
                                       "}")
        self.intro_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.intro_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.intro_frame.setLineWidth(0)
        self.intro_frame.setObjectName("intro_frame")
        self.verticalLayout_3.addWidget(self.intro_frame)
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.intro_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        # Weird "space" (is a transparent button) at top for exiting the app
        self.exit_app_btn = QtWidgets.QPushButton(parent=self.intro_frame)
        self.exit_app_btn.setStyleSheet("background-color: transparent;")
        self.exit_app_btn.setText("")
        self.exit_app_btn.setObjectName("exit_app_btn")
        self.verticalLayout_4.addWidget(self.exit_app_btn)
        
        self.intro_labels = QtWidgets.QFrame(parent=self.intro_frame)
        self.intro_labels.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.intro_labels.setStyleSheet("#intro_labels {\n"
                                        "position: relative;\n"
                                        "height: 100%;\n"
                                        "}\n"
                                        "#intro_lbl_image {\n"
                                        "position: relative;\n"
                                        "top: 0;\n"
                                        "height: 100%;\n"
                                        "}\n"
                                        "#intro_lbl_tagline {\n"
                                        "position: relative;\n"
                                        "}\n"
                                        "#tutorial_label {\n"
                                        "position: relative;\n"
                                        "}\n")
        self.intro_labels.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.intro_labels.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.intro_labels.setLineWidth(0)
        self.intro_labels.setObjectName("intro_labels")
        self.verticalLayout_4.addWidget(self.intro_labels, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.intro_labels)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        # QuickSnap Logo at center
        self.intro_lbl_image = QtWidgets.QLabel(parent=self.intro_labels)
        self.intro_lbl_image.setText("")
        self.intro_lbl_image.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\quicksnap_logo-removebg-preview.png")))
        self.intro_lbl_image.setScaledContents(False)
        self.intro_lbl_image.setObjectName("intro_lbl_image")
        self.verticalLayout_5.addWidget(self.intro_lbl_image, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        # "Picture perfect moments with QuickSnap" Label at center
        self.intro_lbl_tagline = QtWidgets.QLabel(parent=self.intro_labels)
        self.intro_lbl_tagline.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.intro_lbl_tagline.setFont(font)
        self.intro_lbl_tagline.setStyleSheet("color: rgb(255, 255, 255);")
        self.intro_lbl_tagline.setScaledContents(True)
        self.intro_lbl_tagline.setObjectName("intro_lbl_tagline")
        self.verticalLayout_5.addWidget(self.intro_lbl_tagline)
        
        self.frame = QtWidgets.QFrame(parent=self.intro_labels)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5.addWidget(self.frame)
        
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        # "Start QuickSnap" Button at center
        self.intro_btn_start = QtWidgets.QPushButton(parent=self.frame)
        self.intro_btn_start.setFont(font)
        self.intro_btn_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.intro_btn_start.setStyleSheet("#intro_btn_start{\n"
                                           "    background-color: rgb(240, 212, 0);\n"
                                           "    color: rgb(0, 29, 61);\n"
                                           "    border-radius: 10px;\n"
                                           "    height: 80px;\n"
                                           "}\n"
                                           "#intro_btn_start:hover{\n"
                                           "    background-color: rgb(255, 162, 5);\n"
                                           "    color:#fff;\n"
                                           "}")
        self.intro_btn_start.setObjectName("intro_btn_start")
        self.verticalLayout_6.addWidget(self.intro_btn_start)
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        # Label with instructions at center
        self.label_101 = QtWidgets.QLabel(parent=self.intro_labels)
        self.label_101.setFont(font)
        self.label_101.setStyleSheet("color: #fff;")
        self.label_101.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_101.setObjectName("label_101")
        self.verticalLayout_5.addWidget(self.label_101)
        
        self.widget = QtWidgets.QWidget(parent=self.intro_frame)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        
        self.gridLayout_24 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_24.setObjectName("gridLayout_24")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        
        # "i" Button at bottom-right
        self.btnINFO_intro = QtWidgets.QPushButton(parent=self.widget)
        self.btnINFO_intro.setMinimumSize(QtCore.QSize(100, 100))
        self.btnINFO_intro.setMaximumSize(QtCore.QSize(100, 100))
        self.btnINFO_intro.setFont(font)
        self.btnINFO_intro.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnINFO_intro.setStyleSheet("background-color: rgb(0, 29, 61);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border:10px solid rgb(255, 227, 90);\n"
                                            "width: 100px;\n"
                                            "height: 100px;\n"
                                            "border-radius: 50px;\n"
                                            "font-weight:bold;")
        self.btnINFO_intro.setObjectName("btnINFO_intro")
        self.gridLayout_24.addWidget(self.btnINFO_intro, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.stackedWidget.addWidget(self.intro)

    # index 1: Format Formal/Beauty Page (Belic)
    def __init_capture_method_page(self):
        # Widget for the whole page
        self.purpose = QtWidgets.QWidget()
        self.purpose.setStyleSheet("")
        self.purpose.setObjectName("purpose")
        
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.purpose)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        # Frame with QuickSnap background
        self.purpose_frame = QtWidgets.QFrame(parent=self.purpose)
        self.purpose_frame.setStyleSheet("#purpose_frame {\n"
                                         "border-image: url('" + resource_path("package\\resource\\img\\main_bg.png").replace("\\", "/") + "') 0 0 0 0 stretch stretch;\n"
                                         "}")
        self.purpose_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.purpose_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.purpose_frame.setObjectName("purpose_frame")
        self.verticalLayout_7.addWidget(self.purpose_frame)
        
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.purpose_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.purpose_header = QtWidgets.QFrame(parent=self.purpose_frame)
        self.purpose_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.purpose_header.setStyleSheet("#backPurposeButton {\n"
                                          "    qproperty-icon: url('" + resource_path("package\\resource\\img\\back.png").replace("\\", "/") + "');\n"
                                          "    qproperty-iconSize: 30px 30px;\n"
                                          "    background-color: transparent;\n"
                                          "    \n"
                                          "}")
        self.purpose_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.purpose_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.purpose_header.setObjectName("purpose_header")
        self.verticalLayout_8.addWidget(self.purpose_header)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.purpose_header)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        
        # Back Button at top-left
        self.backPurposeButton = QtWidgets.QPushButton(parent=self.purpose_header)
        self.backPurposeButton.setMinimumSize(QtCore.QSize(100, 100))
        self.backPurposeButton.setMaximumSize(QtCore.QSize(100, 100))
        self.backPurposeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backPurposeButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:0.769, y2:0.5685, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border:10px solid rgb(255, 227, 90);\n"
                                            "width: 100px;\n"
                                            "height: 100px;\n"
                                            "border-radius: 50px;\n"
                                            "font-weight:bold;")
        self.backPurposeButton.setText("")
        self.backPurposeButton.setObjectName("backPurposeButton")
        self.gridLayout_10.addWidget(self.backPurposeButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.purpose_content = QtWidgets.QFrame(parent=self.purpose_frame)
        self.purpose_content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.purpose_content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.purpose_content.setObjectName("purpose_content")
        self.verticalLayout_8.addWidget(self.purpose_content)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.purpose_content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.purpose_formal = QtWidgets.QFrame(parent=self.purpose_content)
        self.purpose_formal.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.purpose_formal.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.purpose_formal.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.purpose_formal.setLineWidth(0)
        self.purpose_formal.setObjectName("purpose_formal")
        self.horizontalLayout.addWidget(self.purpose_formal)
        
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.purpose_formal)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        
        # Formal Box Container at the left selection
        self.pFormal_Container = QtWidgets.QFrame(parent=self.purpose_formal)
        self.pFormal_Container.setMaximumSize(QtCore.QSize(400, 600))
        self.pFormal_Container.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.pFormal_Container.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                             "border-radius: 18px;")
        self.pFormal_Container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.pFormal_Container.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.pFormal_Container.setLineWidth(0)
        self.pFormal_Container.setObjectName("pFormal_Container")
        self.verticalLayout_10.addWidget(self.pFormal_Container)
        
        # Formal Image at the left selection
        self.label = QtWidgets.QLabel(parent=self.pFormal_Container)
        self.label.setGeometry(QtCore.QRect(100, 120, 200, 200))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\formal.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        # "Formal" Label at left selection
        self.label_2 = QtWidgets.QLabel(parent=self.pFormal_Container)
        self.label_2.setGeometry(QtCore.QRect(50, 340, 291, 40))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: transparent;\n"
                                   "color: rgb(0, 29, 61);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        # "Great for 1x1 and 2x2 photos" Label at left selection
        self.label_3 = QtWidgets.QLabel(parent=self.pFormal_Container)
        self.label_3.setGeometry(QtCore.QRect(70, 380, 250, 60))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
                                   "color: rgb(0, 29, 61);")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
  
        # Formal Button
        self.btn_Formal = QtWidgets.QPushButton(parent=self.pFormal_Container)
        self.btn_Formal.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.btn_Formal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_Formal.setStyleSheet("background-color: transparent;")
        self.btn_Formal.setText("")
        self.btn_Formal.setObjectName("btn_Formal")

        self.purpose_beauty = QtWidgets.QFrame(parent=self.purpose_content)
        self.purpose_beauty.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.purpose_beauty.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.purpose_beauty.setLineWidth(0)
        self.purpose_beauty.setObjectName("purpose_beauty")
        self.horizontalLayout.addWidget(self.purpose_beauty)
        
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.purpose_beauty)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        
        # Beauty Box Container at the left selection
        self.pBeauty_Container = QtWidgets.QFrame(parent=self.purpose_beauty)
        self.pBeauty_Container.setMaximumSize(QtCore.QSize(400, 600))
        self.pBeauty_Container.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pBeauty_Container.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                             "border-radius: 18px;")
        self.pBeauty_Container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.pBeauty_Container.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.pBeauty_Container.setLineWidth(0)
        self.pBeauty_Container.setObjectName("pBeauty_Container")
        self.verticalLayout_11.addWidget(self.pBeauty_Container)
        
        # Beauty Image at right selection
        self.label_4 = QtWidgets.QLabel(parent=self.pBeauty_Container)
        self.label_4.setGeometry(QtCore.QRect(110, 120, 200, 200))
        self.label_4.setStyleSheet("background-color: transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\beauty.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        # "Beauty" Label at right selection
        self.label_5 = QtWidgets.QLabel(parent=self.pBeauty_Container)
        self.label_5.setGeometry(QtCore.QRect(60, 340, 291, 40))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent;\n"
                                   "color: rgb(0, 29, 61);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # "Great for selfie and groupie" Label at right selection
        self.label_6 = QtWidgets.QLabel(parent=self.pBeauty_Container)
        self.label_6.setGeometry(QtCore.QRect(80, 380, 250, 60))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: transparent;\n"
                                   "color: rgb(0, 29, 61);")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        
        # Beauty Button
        self.btn_Beauty = QtWidgets.QPushButton(parent=self.pBeauty_Container)
        self.btn_Beauty.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.btn_Beauty.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_Beauty.setStyleSheet("background-color: transparent;")
        self.btn_Beauty.setText("")
        self.btn_Beauty.setObjectName("btn_Beauty")

        self.widget_2 = QtWidgets.QWidget(parent=self.purpose_frame)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 151))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_8.addWidget(self.widget_2)
        
        self.gridLayout_25 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_25.setObjectName("gridLayout_25")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        # "i" Button at bottom-right
        self.btnINFO_purpose = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnINFO_purpose.setMinimumSize(QtCore.QSize(100, 100))
        self.btnINFO_purpose.setMaximumSize(QtCore.QSize(100, 100))
        self.btnINFO_purpose.setFont(font)
        self.btnINFO_purpose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnINFO_purpose.setStyleSheet("background-color: rgb(0, 29, 61);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border:10px solid rgb(255, 227, 90);\n"
                                           "width: 100px;\n"
                                           "height: 100px;\n"
                                           "border-radius: 50px;\n"
                                           "font-weight:bold;")
        self.btnINFO_purpose.setObjectName("btnINFO_purpose")
        self.gridLayout_25.addWidget(self.btnINFO_purpose, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.stackedWidget.addWidget(self.purpose)

    # index 2: Gender Page (Tajada)
    def __init_gender_selection_page(self):
        # Widget for the whole page
        self.gender = QtWidgets.QWidget()
        self.gender.setObjectName("gender")
        
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.gender)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        
        # Black Film Strip overlay on the background
        self.gender_frame = QtWidgets.QFrame(parent=self.gender)
        self.gender_frame.setStyleSheet("#gender_frame {\n"
                                        "    border-image: url('" + resource_path("package\\resource\\img\\bg_film2.png").replace("\\", "/") + "') 0 0 0 0 stretch stretch;\n"
                                        "}")
        self.gender_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gender_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gender_frame.setLineWidth(0)
        self.gender_frame.setObjectName("gender_frame")
        self.verticalLayout_21.addWidget(self.gender_frame)

        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.gender_frame)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")

        self.gender_header = QtWidgets.QFrame(parent=self.gender_frame)
        self.gender_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.gender_header.setStyleSheet("#backGenderButton {\n"
                                         "    qproperty-icon: url('" + resource_path("package\\resource\\img\\back.png").replace("\\", "/") + "');\n"
                                         "    qproperty-iconSize: 30px 30px;\n"
                                         "}")
        self.gender_header.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gender_header.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gender_header.setLineWidth(0)
        self.gender_header.setObjectName("gender_header")
        self.verticalLayout_36.addWidget(self.gender_header)

        self.gridLayout_26 = QtWidgets.QGridLayout(self.gender_header)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName("gridLayout_26")

        # Back Button at top-left
        self.backGenderButton = QtWidgets.QPushButton(parent=self.gender_header)
        self.backGenderButton.setMinimumSize(QtCore.QSize(100, 100))
        self.backGenderButton.setMaximumSize(QtCore.QSize(100, 100))
        self.backGenderButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backGenderButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:0.769, y2:0.5685, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border:10px solid rgb(255, 227, 90);\n"
                                            "width: 100px;\n"
                                            "height: 100px;\n"
                                            "border-radius: 50px;\n"
                                            "font-weight:bold;")
        self.backGenderButton.setText("")
        self.backGenderButton.setObjectName("backGenderButton")
        self.gridLayout_26.addWidget(self.backGenderButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.gender_content = QtWidgets.QFrame(parent=self.gender_frame)
        self.gender_content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.gender_content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gender_content.setObjectName("gender_content")
        self.verticalLayout_36.addWidget(self.gender_content)
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.gender_content)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.gender_male = QtWidgets.QFrame(parent=self.gender_content)
        self.gender_male.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.gender_male.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.gender_male.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gender_male.setObjectName("gender_male")
        self.horizontalLayout_6.addWidget(self.gender_male)
        
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.gender_male)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        
        # Male Box Container at the left selection
        self.gMale_container = QtWidgets.QFrame(parent=self.gender_male)
        self.gMale_container.setMaximumSize(QtCore.QSize(400, 600))
        self.gMale_container.setStyleSheet("#gMale_container{background-color: rgba(255, 255, 255,0.8);border-radius: 18px;}")
        self.gMale_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.gMale_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gMale_container.setObjectName("gMale_container")
        self.verticalLayout_37.addWidget(self.gMale_container)
        
        # Male Image at the left selection
        self.label_102 = QtWidgets.QLabel(parent=self.gMale_container)
        self.label_102.setGeometry(QtCore.QRect(40, 90, 321, 341))
        self.label_102.setText("")
        self.label_102.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\male.png")))
        self.label_102.setScaledContents(True)
        self.label_102.setObjectName("label_102")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        # "Male" Label at the left selection
        self.label_103 = QtWidgets.QLabel(parent=self.gMale_container)
        self.label_103.setGeometry(QtCore.QRect(0, 450, 400, 20))
        self.label_103.setMinimumSize(QtCore.QSize(400, 0))
        self.label_103.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("color: rgb(0, 29, 61);")
        self.label_103.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_103.setObjectName("label_103")

        # Male Button
        self.btnMale = QtWidgets.QPushButton(parent=self.gMale_container)
        self.btnMale.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.btnMale.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnMale.setStyleSheet("border-radius: 18px;\n"
                                   "background-color:transparent;")
        self.btnMale.setText("")
        self.btnMale.setObjectName("btnMale")

        self.gender_female = QtWidgets.QFrame(parent=self.gender_content)
        self.gender_female.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.gender_female.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gender_female.setObjectName("gender_female")
        self.horizontalLayout_6.addWidget(self.gender_female)
        
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.gender_female)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        
        # Female Box Container at the right selection
        self.gFemale_container = QtWidgets.QFrame(parent=self.gender_female)
        self.gFemale_container.setMaximumSize(QtCore.QSize(400, 600))
        self.gFemale_container.setStyleSheet("#gFemale_container{background-color: rgba(255, 255, 255,0.8);border-radius: 18px;}")
        self.gFemale_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.gFemale_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gFemale_container.setObjectName("gFemale_container")
        self.verticalLayout_38.addWidget(self.gFemale_container)
        
        # Female Image at the right selection
        self.label_104 = QtWidgets.QLabel(parent=self.gFemale_container)
        self.label_104.setGeometry(QtCore.QRect(40, 90, 321, 341))
        self.label_104.setText("")
        self.label_104.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\female.png")))
        self.label_104.setScaledContents(True)
        self.label_104.setObjectName("label_104")
        
        # "Female" Label at the right selection
        self.label_105 = QtWidgets.QLabel(parent=self.gFemale_container)
        self.label_105.setGeometry(QtCore.QRect(0, 450, 400, 20))
        self.label_105.setMinimumSize(QtCore.QSize(400, 0))
        self.label_105.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("color: rgb(0, 29, 61);")
        self.label_105.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_105.setObjectName("label_105")
        
        # Female Button
        self.btnFemale = QtWidgets.QPushButton(parent=self.gFemale_container)
        self.btnFemale.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.btnFemale.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnFemale.setStyleSheet("border-radius: 18px;\n"
                                     "background-color:transparent;")
        self.btnFemale.setText("")
        self.btnFemale.setObjectName("btnFemale")
        
        self.widget_3 = QtWidgets.QWidget(parent=self.gender_frame)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 151))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 151))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_36.addWidget(self.widget_3)
        
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        # "i" Button at bottom-right
        self.btnINFO_gender = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnINFO_gender.setMinimumSize(QtCore.QSize(100, 100))
        self.btnINFO_gender.setMaximumSize(QtCore.QSize(100, 100))
        self.btnINFO_gender.setFont(font)
        self.btnINFO_gender.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnINFO_gender.setStyleSheet("background-color: rgb(0, 29, 61);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:10px solid rgb(255, 227, 90);\n"
                                          "width: 100px;\n"
                                          "height: 100px;\n"
                                          "border-radius: 50px;\n"
                                          "font-weight:bold;")
        self.btnINFO_gender.setObjectName("btnINFO_gender")
        self.verticalLayout_39.addWidget(self.btnINFO_gender, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.stackedWidget.addWidget(self.gender)

    # index 3: Capture Page Formal (Tajada)
    def __init_formal_capture_page(self):
        # Widget for the whole page
        self.camera = QtWidgets.QWidget()
        self.camera.setStyleSheet("")
        self.camera.setObjectName("camera") #"camera"
        
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.camera)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0) #(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        self.camera_content = QtWidgets.QFrame(parent=self.camera)
        self.camera_content.setStyleSheet("")
        self.camera_content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.camera_content.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.camera_content.setObjectName("camera_content")
        self.verticalLayout_13.addWidget(self.camera_content)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.camera_content)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")

        self.camera_header = QtWidgets.QFrame(parent=self.camera_content)
        self.camera_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.camera_header.setStyleSheet("#backCameraButton {\n"
                                         "    qproperty-icon: url('" + resource_path("package\\resource\\img\\back.png").replace("\\", "/") + "');\n"
                                         "    qproperty-iconSize: 30px 30px;\n"
                                         "}\n"
                                         "#camera_header{\n"
                                         "    \n"
                                         "    background-color: rgb(238, 238, 238);\n"
                                         "}")
        self.camera_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel) #semi colon ;
        self.camera_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.camera_header.setObjectName("camera_header")
        self.verticalLayout_14.addWidget(self.camera_header)

        self.gridLayout_28 = QtWidgets.QGridLayout(self.camera_header)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName("gridLayout_28")

        # Back Button at top-left
        self.backCameraButton = QtWidgets.QPushButton(parent=self.camera_header)
        self.backCameraButton.setMinimumSize(QtCore.QSize(100, 100))
        self.backCameraButton.setMaximumSize(QtCore.QSize(100, 100))
        self.backCameraButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)) # . in self.backCameraButton.
        self.backCameraButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:0.769, y2:0.5685, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border:10px solid rgb(255, 227, 90);\n"
                                            "width: 100px;\n"
                                            "height: 100px;\n"
                                            "border-radius: 50px;\n"
                                            "font-weight:bold;")
        self.backCameraButton.setText("")
        self.backCameraButton.setObjectName("backCameraButton")
        self.gridLayout_28.addWidget(self.backCameraButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.camera_container = QtWidgets.QFrame(parent=self.camera_content)
        self.camera_container.setStyleSheet("#camera_container{\n"
                                            "    background-color: rgb(238, 238, 238);\n"
                                            "}\n"
                                            "#camera_input{\n"
                                            "    margin: 11px 30px;\n"
                                            "}")
        self.camera_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.camera_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.camera_container.setObjectName("camera_container")
        self.verticalLayout_14.addWidget(self.camera_container)
        
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.camera_container) #added = sign
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        
        # Label for the video feed of the camera at center
        self.camera_formal_label = QuickSnapWidget(parent=self.camera_container)
        self.camera_formal_label.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.camera_formal_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.camera_formal_label.setLineWidth(1)
        self.camera_formal_label.setObjectName("camera_formal_label")
        self.verticalLayout_29.addWidget(self.camera_formal_label)

        self.shot_options = QtWidgets.QFrame(parent=self.camera_container)
        self.shot_options.setMaximumSize(QtCore.QSize(16777215, 250))
        self.shot_options.setStyleSheet("")
        self.shot_options.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.shot_options.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.shot_options.setObjectName("shot_options")
        self.verticalLayout_29.addWidget(self.shot_options)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.shot_options)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.frame_5 = QtWidgets.QFrame(parent=self.shot_options)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(110, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        
        # Circle Capture Button at center
        self.capture_formal = QtWidgets.QPushButton(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_formal.sizePolicy().hasHeightForWidth())
        self.capture_formal.setSizePolicy(sizePolicy)
        self.capture_formal.setMinimumSize(QtCore.QSize(180, 180))
        self.capture_formal.setMaximumSize(QtCore.QSize(180, 180))
        self.capture_formal.setFont(font)
        self.capture_formal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.capture_formal.setStyleSheet("border: 10px solid rgba(0, 29, 61, 1);\n"
                                          "background-color: rgba(0, 53, 102, 1);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 90px;\n"
                                          "height: 180px;\n"
                                          "width: 180px;\n"
                                          "font-weight:bold;")
        self.capture_formal.setObjectName("capture_formal")
        self.horizontalLayout_7.addWidget(self.capture_formal)

        self.frame_20 = QtWidgets.QFrame(parent=self.shot_options)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_2.addWidget(self.frame_20, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_27.setContentsMargins(0, 0, 5, 25)
        self.gridLayout_27.setObjectName("gridLayout_27")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        
        # "i" Button at bottom-right
        self.btnINFO_camera = QtWidgets.QPushButton(parent=self.frame_20)
        self.btnINFO_camera.setMinimumSize(QtCore.QSize(100, 100))
        self.btnINFO_camera.setMaximumSize(QtCore.QSize(100, 100))
        self.btnINFO_camera.setFont(font)
        self.btnINFO_camera.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnINFO_camera.setStyleSheet("background-color: rgb(0, 29, 61);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:10px solid rgb(255, 227, 90);\n"
                                          "width: 100px;\n"
                                          "height: 100px;\n"
                                          "border-radius: 50px;\n"
                                          "font-weight:bold;")
        self.btnINFO_camera.setObjectName("btnINFO_camera")
        self.gridLayout_27.addWidget(self.btnINFO_camera, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        
        self.horizontalLayout_2.setStretch(0, 1)

        self.stackedWidget.addWidget(self.camera)

    # index 4: Capture Page Beauty (Samson)
    #def __init_beauty_capture_page(self):h wrong
    def __init_beauty_capture_page(self):
        # Widget for the whole page
        self.filters = QtWidgets.QWidget()
        self.filters.setObjectName("filters")
        
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.filters)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        
        self.filters_frame = QtWidgets.QFrame(parent=self.filters)
        self.filters_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.filters_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.filters_frame.setObjectName("filters_frame")
        self.verticalLayout_15.addWidget(self.filters_frame)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.filters_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        # Filter Panel Container at left side of screen
        self.filter_container = QtWidgets.QFrame(parent=self.filters_frame)
        self.filter_container.setMinimumSize(QtCore.QSize(300, 0))
        self.filter_container.setMaximumSize(QtCore.QSize(300, 16777215))
        self.filter_container.setStyleSheet("#filter_container{background-color: qlineargradient(spread:reflect, x1:0.507463, y1:1, x2:0.488, y2:0.506, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));}")
        self.filter_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.filter_container.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.filter_container.setLineWidth(0)
        self.filter_container.setObjectName("filter_container")
        self.horizontalLayout_3.addWidget(self.filter_container)
        
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.filter_container)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        
        self.frame_10 = QtWidgets.QFrame(parent=self.filter_container)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_10.setStyleSheet("#backFilterButton {\n"
                                    "    qproperty-icon: url('" + resource_path("package\\resource\\img\\back.png").replace("\\", "/") + "');\n"
                                    "    qproperty-iconSize: 30px 30px;\n"
                                    "    background-color: transparent;\n"
                                    "    \n"
                                    "}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_17.addWidget(self.frame_10)
        
        self.gridLayout_31 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_31.setObjectName("gridLayout_31")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_10 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_31.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.frame_14 = QtWidgets.QFrame(parent=self.filter_container)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_17.addWidget(self.frame_14)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.frame_16 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_16.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_16.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_16.setStyleSheet("")
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_4.addWidget(self.frame_16)
        
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName("verticalLayout_32")

        # White Bars in the left side of the Filter Film Strip (Filter Panel Container)
        for i in range(30):
            label_temp = QtWidgets.QLabel(parent=self.frame_16)
            label_temp.setMinimumSize(QtCore.QSize(30, 15))
            label_temp.setMaximumSize(QtCore.QSize(30, 15))
            label_temp.setStyleSheet("background-color: rgb(255, 255, 255);")
            label_temp.setText("")
            label_temp.setObjectName("label_" + str(64 + i))
            self.verticalLayout_32.addWidget(label_temp)

        self.frame_18 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_4.addWidget(self.frame_18)
        
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        
        # Scroll UI for Filters (hidden but still working)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_18)
        self.scrollArea.setStyleSheet("background-color: transparent;\n"
                                      "width: 0px;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setLineWidth(-3) #Line980-Quote
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.gridLayout_23.addWidget(self.scrollArea, 0, 0, 1, 1)
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 216, 1965))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_34.setContentsMargins(15, 15, 15, 15) #Line992-dot
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        
        # Filter Dynamic Initialization START (Ocampo)
        filters_dict = {
            "cheek": {
                "blush": ("package\\resource\\filter\\icon\\blush_icon.jpg", "package\\resource\\filter\\background\\blush_bg.jpg", "package\\resource\\filter\\cheek\\blush.png"),
                "grizzly": ("package\\resource\\filter\\icon\\grizzly_icon.jpg", "package\\resource\\filter\\background\\grizzly_bg.jpg", "package\\resource\\filter\\cheek\\grizzly.png"),
                "pinkheart": ("package\\resource\\filter\\icon\\pinkheart_icon.jpg", "package\\resource\\filter\\background\\pinkheart_bg.jpg", "package\\resource\\filter\\cheek\\pinkheart.png")
            }
        }

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        filter_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(filter_button.sizePolicy().hasHeightForWidth())
        filter_button.setSizePolicy(sizePolicy)
        filter_button.setMinimumSize(QtCore.QSize(180, 180))
        filter_button.setMaximumSize(QtCore.QSize(180, 180))
        filter_button.setStyleSheet("border-image: url('" + resource_path("package/resource/img/null.png").replace("\\", "/") + "');")
        filter_button.setText("")
        filter_button.setObjectName("filter_null_null")
        filter_button.clicked.connect(partial(self.__handle_filter, "null", None, None))
        self.verticalLayout_34.addWidget(filter_button)
        
        for key_location, value_location in filters_dict.items():
            for key_filter, value_filter in value_location.items():
                filter_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
                sizePolicy.setHeightForWidth(filter_button.sizePolicy().hasHeightForWidth())
                filter_button.setSizePolicy(sizePolicy)
                filter_button.setMinimumSize(QtCore.QSize(180, 180))
                filter_button.setMaximumSize(QtCore.QSize(180, 180))
                filter_button.setStyleSheet("border-image: url('" + resource_path(value_filter[0]).replace("\\", "/") + "');")
                filter_button.setText("") #Line1022-SEMICOLON
                filter_button.setObjectName(f"filter_{key_location}_{key_filter}")
                filter_button.clicked.connect(partial(self.__handle_filter, key_location, value_filter[1], value_filter[2]))
                self.verticalLayout_34.addWidget(filter_button)
        # Filter Dynamic Initialization END (Ocampo)
        
        self.frame_17 = QtWidgets.QFrame(parent=self.frame_14) #Line1029-DoubleEqual
        self.frame_17.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_17.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_17.setStyleSheet("")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_4.addWidget(self.frame_17)
        
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_17) #Line1037SingleEqualOnly
        self.verticalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName("verticalLayout_33")

        # White Bars in the right side of the Filter Film Strip (Filter Panel Container)
        for i in range(30):
            label_temp = QtWidgets.QLabel(parent=self.frame_17)
            label_temp.setMinimumSize(QtCore.QSize(30, 15))
            label_temp.setMaximumSize(QtCore.QSize(30, 15))
            label_temp.setStyleSheet("background-color: rgb(255, 255, 255);")
            label_temp.setText("")
            label_temp.setObjectName("label_" + str(80 + i))
            self.verticalLayout_33.addWidget(label_temp)

        self.filter_cam_container = QtWidgets.QFrame(parent=self.filters_frame)
        self.filter_cam_container.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.filter_cam_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.filter_cam_container.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.filter_cam_container.setLineWidth(0)
        self.filter_cam_container.setObjectName("filter_cam_container")
        self.horizontalLayout_3.addWidget(self.filter_cam_container)

        self.gridLayout_29 = QtWidgets.QGridLayout(self.filter_cam_container)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName("gridLayout_29")

        self.filter_shot_option = QtWidgets.QFrame(parent=self.filter_cam_container)
        self.filter_shot_option.setMaximumSize(QtCore.QSize(16777215, 250))
        self.filter_shot_option.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.filter_shot_option.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.filter_shot_option.setObjectName("filter_shot_option")
        self.gridLayout_29.addWidget(self.filter_shot_option, 2, 0, 1, 1)

        # Label for the video feed of the camera at center
        self.camera_beauty_label = QuickSnapWidget(parent=self.filter_cam_container)
        self.gridLayout_29.addWidget(self.camera_beauty_label, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.filter_shot_option)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.frame_21 = QtWidgets.QFrame(parent=self.filter_shot_option)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_8.addWidget(self.frame_21)
        
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        
        # Circle Capture Button at center
        self.capture_beauty = QtWidgets.QPushButton(parent=self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_beauty.sizePolicy().hasHeightForWidth())
        self.capture_beauty.setSizePolicy(sizePolicy)
        self.capture_beauty.setMaximumSize(QtCore.QSize(180, 180))
        self.capture_beauty.setFont(font)
        self.capture_beauty.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.capture_beauty.setStyleSheet("border: 10px solid rgba(0, 29, 61, 1);\n"
                                          "background-color: rgba(0, 53, 102, 1);\n"
                                          "color:#fff;\n"
                                          "border-radius: 90px;\n"
                                          "height: 180px;\n"
                                          "width: 180px;;\n"
                                          "font-weight:bold;")
        self.capture_beauty.setObjectName("capture_beauty")
        self.horizontalLayout_9.addWidget(self.capture_beauty)
        
        self.frame_15 = QtWidgets.QFrame(parent=self.filter_shot_option)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8.addWidget(self.frame_15, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_22.setContentsMargins(0, 0, 5, 25)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        
        # "i" Button at bottom-right
        self.btnINFO_filter = QtWidgets.QPushButton(parent=self.frame_15)
        self.btnINFO_filter.setMinimumSize(QtCore.QSize(100, 100))
        self.btnINFO_filter.setMaximumSize(QtCore.QSize(100, 100))
        self.btnINFO_filter.setFont(font)
        self.btnINFO_filter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnINFO_filter.setStyleSheet("background-color: rgb(0, 29, 61);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border:10px solid rgb(255, 227, 90);\n"
                                          "width: 100px;\n"
                                          "height: 100px;\n"
                                          "border-radius: 50px;\n"
                                          "font-weight:bold;")
        self.btnINFO_filter.setObjectName("btnINFO_filter")
        self.gridLayout_22.addWidget(self.btnINFO_filter, 0, 0, 1, 1)
        
        self.horizontalLayout_8.setStretch(0, 1)
        
        self.filter_header = QtWidgets.QFrame(parent=self.filter_cam_container)
        self.filter_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.filter_header.setStyleSheet("#backFilterButton {\n"
                                         "    qproperty-icon: url('" + resource_path("package\\resource\\img\\back.png").replace("\\", "/") + "');\n"
                                         "    qproperty-iconSize: 30px 30px;\n"
                                         "}\n"
                                         "#filter_header{\n"
                                         "background-color: rgb(238, 238, 238);\n"
                                         "}")
        self.filter_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.filter_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.filter_header.setObjectName("filter_header")
        self.gridLayout_29.addWidget(self.filter_header, 0, 0, 1, 1)
        
        self.gridLayout_30 = QtWidgets.QGridLayout(self.filter_header)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        
        # Back Button at top-left
        self.backFilterButton = QtWidgets.QPushButton(parent=self.filter_header)
        self.backFilterButton.setMinimumSize(QtCore.QSize(100, 100))
        self.backFilterButton.setMaximumSize(QtCore.QSize(100, 100))
        self.backFilterButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backFilterButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:0.769, y2:0.5685, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border:10px solid rgb(255, 227, 90);\n"
                                            "width: 100px;\n"
                                            "height: 100px;\n"
                                            "border-radius: 50px;\n"
                                            "font-weight:bold;")
        self.backFilterButton.setText("")
        self.backFilterButton.setObjectName("backFilterButton")
        self.gridLayout_30.addWidget(self.backFilterButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.stackedWidget.addWidget(self.filters)

    # index 5: Retake/Finish Page (Barbachano)
    def __init_capture_preview_page(self):
        # Widget for the whole page
        self.finish = QtWidgets.QWidget()
        self.finish.setObjectName("finish") # removed finish
        
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.finish)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        
        # Frame with QuickSnap background
        self.finish_frame = QtWidgets.QFrame(parent=self.finish)
        self.finish_frame.setStyleSheet("#finish_frame{\n"
                                        "border-image: url('" + resource_path("package\\resource\\img\\main_bg.png").replace("\\", "/") + "');\n"
                                        "}")
        self.finish_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.finish_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.finish_frame.setObjectName("finish_frame")
        self.verticalLayout_20.addWidget(self.finish_frame)
        
        self.gridLayout_15 = QtWidgets.QGridLayout(self.finish_frame)
        self.gridLayout_15.setObjectName("gridLayout_15")
        
        self.finish_container = QtWidgets.QFrame(parent=self.finish_frame)
        self.finish_container.setMaximumSize(QtCore.QSize(1000, 800)) # added dot (.)
        self.finish_container.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                            "border-radius: 18px;")
        self.finish_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.finish_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.finish_container.setObjectName("finish_container")
        self.gridLayout_15.addWidget(self.finish_container, 0, 0, 1, 1)
        
        self.gridLayout_17 = QtWidgets.QGridLayout(self.finish_container) # added =
        self.gridLayout_17.setObjectName("gridLayout_17")
        
        self.frame_8 = QtWidgets.QFrame(parent=self.finish_container)
        self.frame_8.setMaximumSize(QtCore.QSize(800, 600))
        self.frame_8.setStyleSheet("background-color: transparent;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_17.addWidget(self.frame_8, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_22.setSpacing(20) # removed 20 in setSpacing
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        
        # Image that contains the captured photo at center
        self.captured_frame_label = QtWidgets.QLabel(parent=self.frame_8) # missing ) syntax
        self.captured_frame_label.setText("")
        self.captured_frame_label.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\camera.png")))
        self.captured_frame_label.setObjectName("captured_frame_label")
        self.verticalLayout_22.addWidget(self.captured_frame_label)
        
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_9.setStyleSheet("#btn_retake, #btn_finish{\n"
                                   "    background-color: rgb(240, 212, 0);\n"
                                   "    color: rgb(0, 29, 61);\n"
                                   "    border-radius: 10px;\n"
                                   "    height: 100px;\n"
                                   "}\n"
                                   "#btn_retake:hover, #btn_finish:hover{\n"
                                   "    background-color: rgb(255, 162, 5);\n"
                                   "    color:#fff;\n"
                                   "}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_22.addWidget(self.frame_9)
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)

        # "Retake" Button at center
        self.btn_retake = QtWidgets.QPushButton(parent=self.frame_9)
        self.btn_retake.setFont(font)
        self.btn_retake.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_retake.setStyleSheet("")
        self.btn_retake.setObjectName("btn_retake")
        self.horizontalLayout_5.addWidget(self.btn_retake)

        # "Finish" Button at center
        self.btn_finish = QtWidgets.QPushButton(parent=self.frame_9)
        self.btn_finish.setFont(font)
        self.btn_finish.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_finish.setStyleSheet("")
        self.btn_finish.setObjectName("btn_finish")
        self.horizontalLayout_5.addWidget(self.btn_finish)

        self.stackedWidget.addWidget(self.finish)

    # index 6: Package Page (Barbachano)
    def __init_package_selection_page(self):
        # Widget for the whole page, with the yellow gradient background
        self.style = QtWidgets.QWidget()
        self.style.setStyleSheet("#style {\n"
                                 "border-image: url('" + resource_path("package\\resource\\img\\bg_gradient.png").replace("\\", "/") + "') 0 0 0 0 stretch stretch;\n"
                                 "}")
        self.style.setObjectName("style")

        # Black Border on the background
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.style)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        
        self.style_frame = QtWidgets.QFrame(parent=self.style)
        self.style_frame.setStyleSheet("#style_frame {\n"
                                     "border-image: url('" + resource_path("package\\resource\\img\\bg_film3.png").replace("\\", "/") + "') 0 0 0 0 stretch stretch;\n"
                                     "}")
        self.style_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.style_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.style_frame.setObjectName("style_frame")
        self.verticalLayout_16.addWidget(self.style_frame)
        
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.style_frame)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        
        self.style_header = QtWidgets.QFrame(parent=self.style_frame)
        self.style_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.style_header.setStyleSheet("#backStyleButton {\n"
                                        "    qproperty-icon: url('" + resource_path("package\\resource\\img\\back.png").replace("\\", "/") + "');\n"
                                        "    qproperty-iconSize: 30px 30px;\n"
                                        "    background-color: transparent;\n"
                                        "    \n"
                                        "}")
        self.style_header.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.style_header.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.style_header.setLineWidth(0)
        self.style_header.setObjectName("style_header")
        self.verticalLayout_18.addWidget(self.style_header)
        
        self.gridLayout_9 = QtWidgets.QGridLayout(self.style_header)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        
        # Back button at top-left
        self.backStyleButton = QtWidgets.QPushButton(parent=self.style_header)
        self.backStyleButton.setMinimumSize(QtCore.QSize(100, 100))
        self.backStyleButton.setMaximumSize(QtCore.QSize(100, 100))
        self.backStyleButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backStyleButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:0.769, y2:0.5685, stop:0 rgba(255, 214, 10, 255), stop:1 rgba(255, 114, 0, 255));\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border:10px solid rgb(255, 227, 90);\n"
                                            "width: 100px;\n"
                                            "height: 100px;\n"
                                            "border-radius: 50px;\n"
                                            "font-weight:bold;")
        self.backStyleButton.setText("")
        self.backStyleButton.setObjectName("backStyleButton")
        self.gridLayout_9.addWidget(self.backStyleButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.style_packages = QtWidgets.QFrame(parent=self.style_frame)
        self.style_packages.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.style_packages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.style_packages.setObjectName("style_packages")
        self.verticalLayout_18.addWidget(self.style_packages)
        
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.style_packages)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_19.setStretch(0, 2)
        self.verticalLayout_19.setStretch(1, 2)
        self.verticalLayout_19.setStretch(2, 1)
        
        self.frame_3 = QtWidgets.QFrame(parent=self.style_packages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("")
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_19.addWidget(self.frame_3)
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_2.setHorizontalSpacing(19)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.styleA_frame = QtWidgets.QFrame(parent=self.frame_3)
        self.styleA_frame.setMinimumSize(QtCore.QSize(600, 350))
        self.styleA_frame.setMaximumSize(QtCore.QSize(600, 350))
        self.styleA_frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.styleA_frame.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.styleA_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.styleA_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.styleA_frame.setLineWidth(0)
        self.styleA_frame.setObjectName("styleA_frame")
        self.gridLayout_2.addWidget(self.styleA_frame, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.styleA_frame.raise_()
        
        self.gridLayout = QtWidgets.QGridLayout(self.styleA_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Package A Box Container
        self.package_A = QtWidgets.QFrame(parent=self.styleA_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.package_A.sizePolicy().hasHeightForWidth())
        self.package_A.setSizePolicy(sizePolicy)
        self.package_A.setMinimumSize(QtCore.QSize(600, 350))
        self.package_A.setMaximumSize(QtCore.QSize(600, 350))
        self.package_A.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.package_A.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                     "border-radius: 12px;")
        self.package_A.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.package_A.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.package_A.setLineWidth(0)
        self.package_A.setObjectName("package_A")
        self.gridLayout.addWidget(self.package_A, 0, 0, 1, 1)
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.package_A)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.frame_2 = QtWidgets.QFrame(parent=self.package_A)
        self.frame_2.setStyleSheet("background-color: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        # Package A Images START
        self.label_18 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_18.setMaximumSize(QtCore.QSize(100, 100))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        
        self.label_15 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_15.setMaximumSize(QtCore.QSize(100, 100))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)
        
        self.label_16 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_16.setMaximumSize(QtCore.QSize(100, 100))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 0, 2, 1, 1)
        
        self.label_14 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_14.setMaximumSize(QtCore.QSize(100, 100))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 3, 1, 1)
        
        self.label_17 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_17.setMaximumSize(QtCore.QSize(100, 100))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 2, 1, 1)
        
        self.label_19 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_19.setMaximumSize(QtCore.QSize(100, 100))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 1, 1, 1)
        
        self.label_20 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_20.setMaximumSize(QtCore.QSize(100, 100))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 3, 1, 1)
        
        self.label_21 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_21.setMaximumSize(QtCore.QSize(100, 100))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)
        # Package A Images END
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # "Package A : 8 pcs 1x1 photos" Label
        self.package_A_title = QtWidgets.QPushButton(parent=self.package_A)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.package_A_title.sizePolicy().hasHeightForWidth())
        self.package_A_title.setSizePolicy(sizePolicy)
        self.package_A_title.setMinimumSize(QtCore.QSize(0, 60))
        self.package_A_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.package_A_title.setFont(font)
        self.package_A_title.setStyleSheet("padding: 5px 0px;\n"
                                          "background-color: transparent;\n"
                                          "color: rgb(0, 29, 61);\n"
                                          "font-weight: bold;")
        self.package_A_title.setObjectName("package_A_title")
        self.gridLayout_4.addWidget(self.package_A_title, 0, 0, 1, 1)
        
        self.styleB_frame = QtWidgets.QFrame(parent=self.frame_3)
        self.styleB_frame.setMinimumSize(QtCore.QSize(600, 350))
        self.styleB_frame.setMaximumSize(QtCore.QSize(600, 350))
        self.styleB_frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.styleB_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.styleB_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.styleB_frame.setLineWidth(0)
        self.styleB_frame.setObjectName("styleB_frame")
        self.gridLayout_2.addWidget(self.styleB_frame, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.styleB_frame.raise_()
        
        self.gridLayout_7 = QtWidgets.QGridLayout(self.styleB_frame)
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        
        # Package B Box Container
        self.package_B = QtWidgets.QFrame(parent=self.styleB_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.package_B.sizePolicy().hasHeightForWidth())
        self.package_B.setSizePolicy(sizePolicy)
        self.package_B.setMinimumSize(QtCore.QSize(600, 350))
        self.package_B.setMaximumSize(QtCore.QSize(600, 350))
        self.package_B.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.package_B.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                     "border-radius: 12px;")
        self.package_B.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.package_B.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.package_B.setLineWidth(0)
        self.package_B.setObjectName("package_B")
        self.gridLayout_7.addWidget(self.package_B, 0, 0, 1, 1)
        
        self.gridLayout_5 = QtWidgets.QGridLayout(self.package_B)
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.frame_4 = QtWidgets.QFrame(parent=self.package_B)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background-color: transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5.addWidget(self.frame_4, 1, 0, 1, 1)
        
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        # Package B Images START
        self.label_24 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_24.setMaximumSize(QtCore.QSize(120, 120))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 0, 2, 1, 1)
        
        self.label_25 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_25.setMaximumSize(QtCore.QSize(120, 120))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 0, 3, 1, 1)
        
        self.label_23 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_23.setMaximumSize(QtCore.QSize(120, 120))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 1, 3, 1, 1)
        
        self.label_22 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_22.setMaximumSize(QtCore.QSize(120, 120))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 1, 2, 1, 1)
        # Package B Images END
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # "Package B : 4 pcs 2x2 photos" Label
        self.package_B_title = QtWidgets.QPushButton(parent=self.package_B)
        self.package_B_title.setMinimumSize(QtCore.QSize(0, 60))
        self.package_B_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.package_B_title.setFont(font)
        self.package_B_title.setStyleSheet("padding: 5px 0px;\n"
                                           "background-color: transparent;\n"
                                           "color: rgb(0, 29, 61);\n"
                                           "font-weight: bold;")
        self.package_B_title.setObjectName("package_B_title")
        self.gridLayout_5.addWidget(self.package_B_title, 0, 0, 1, 1)
        
        self.frame_19 = QtWidgets.QFrame(parent=self.style_packages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_19.addWidget(self.frame_19)
        
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_8.setObjectName("gridLayout_8")
        
        self.styleC_frame = QtWidgets.QFrame(parent=self.frame_19)
        self.styleC_frame.setMinimumSize(QtCore.QSize(600, 350))
        self.styleC_frame.setMaximumSize(QtCore.QSize(600, 350))
        self.styleC_frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.styleC_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.styleC_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.styleC_frame.setObjectName("styleC_frame")
        self.gridLayout_8.addWidget(self.styleC_frame, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.gridLayout_13 = QtWidgets.QGridLayout(self.styleC_frame)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        
        # Package C Box Container
        self.package_C = QtWidgets.QFrame(parent=self.styleC_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.package_C.sizePolicy().hasHeightForWidth())
        self.package_C.setSizePolicy(sizePolicy)
        self.package_C.setMinimumSize(QtCore.QSize(600, 350))
        self.package_C.setMaximumSize(QtCore.QSize(600, 350))
        self.package_C.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.package_C.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                     "border-radius: 12px;")
        self.package_C.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.package_C.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.package_C.setLineWidth(0)
        self.package_C.setObjectName("package_C")
        self.gridLayout_13.addWidget(self.package_C, 0, 0, 1, 1)
        
        self.gridLayout_11 = QtWidgets.QGridLayout(self.package_C)
        self.gridLayout_11.setObjectName("gridLayout_11")
        
        self.frame_6 = QtWidgets.QFrame(parent=self.package_C)
        self.frame_6.setStyleSheet("background-color: transparent;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_11.addWidget(self.frame_6, 2, 0, 1, 1)
        
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        
        # Package C Images START
        self.label_33 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_33.setMaximumSize(QtCore.QSize(100, 100))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.gridLayout_12.addWidget(self.label_33, 1, 0, 1, 1)
        
        self.label_7 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_7.setMaximumSize(QtCore.QSize(100, 100))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_12.addWidget(self.label_7, 1, 3, 1, 1)
        
        self.label_35 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_35.setMaximumSize(QtCore.QSize(100, 100))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.gridLayout_12.addWidget(self.label_35, 1, 1, 1, 1)
        
        self.label_8 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_8.setMaximumSize(QtCore.QSize(100, 100))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_12.addWidget(self.label_8, 1, 2, 1, 1)
        
        self.frame_7 = QtWidgets.QFrame(parent=self.package_C)
        self.frame_7.setStyleSheet("background-color:transparent;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_11.addWidget(self.frame_7, 1, 0, 1, 1)
        
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName("gridLayout_14")
        
        self.label_26 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_26.setMaximumSize(QtCore.QSize(120, 120))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout_14.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(parent=self.frame_7)
        
        self.label_27.setMaximumSize(QtCore.QSize(120, 120))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\man.png")))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.gridLayout_14.addWidget(self.label_27, 0, 1, 1, 1)
        # Package C Images END
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # "Combo : 4 pcs 1x1 & 2 pc 2x2 photos" Label
        self.package_C_title = QtWidgets.QPushButton(parent=self.package_C)
        self.package_C_title.setMinimumSize(QtCore.QSize(0, 60))
        self.package_C_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.package_C_title.setFont(font)
        self.package_C_title.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.package_C_title.setStyleSheet("padding: 5px 0px;\n"
                                           "background-color: transparent;\n"
                                           "color: rgb(0, 29, 61);\n"
                                           "font-weight: bold;")
        self.package_C_title.setObjectName("package_C_title")
        self.gridLayout_11.addWidget(self.package_C_title, 0, 0, 1, 1)
        
        self.widget_4 = QtWidgets.QWidget(parent=self.style_packages)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_19.addWidget(self.widget_4)
        
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_40.setObjectName("verticalLayout_40")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        
        # "i" Button at bottom-right
        self.btnINFO_style = QtWidgets.QPushButton(parent=self.widget_4)
        self.btnINFO_style.setMinimumSize(QtCore.QSize(100, 100))
        self.btnINFO_style.setMaximumSize(QtCore.QSize(100, 100))
        self.btnINFO_style.setFont(font)
        self.btnINFO_style.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnINFO_style.setStyleSheet("background-color: rgb(0, 29, 61);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border:10px solid rgb(255, 227, 90);\n"
                                         "width: 100px;\n"
                                         "height: 100px;\n"
                                         "border-radius: 50px;\n"
                                         "font-weight:bold;")
        self.btnINFO_style.setObjectName("btnINFO_style")
        self.verticalLayout_40.addWidget(self.btnINFO_style, 0, QtCore.Qt.AlignmentFlag.AlignRight)

        self.stackedWidget.addWidget(self.style)

    # index 7
    def __init_printing_page(self):
        self.printing = QtWidgets.QWidget()
        self.printing.setObjectName("printing")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.printing)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.printing_frame = QtWidgets.QFrame(parent=self.printing)
        self.printing_frame.setStyleSheet("#printing_frame{\n"
                                          "border-image: url('" + resource_path("package\\resource\\img\\main_bg.png").replace("\\", "/") + "');\n"
                                          "}")
        self.printing_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.printing_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.printing_frame.setObjectName("printing_frame")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.printing_frame)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.printing_container = QtWidgets.QFrame(parent=self.printing_frame)
        self.printing_container.setMaximumSize(QtCore.QSize(1000, 800))
        self.printing_container.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                              "border-radius: 18px;")
        self.printing_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.printing_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.printing_container.setObjectName("printing_container")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.printing_container)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_11 = QtWidgets.QFrame(parent=self.printing_container)
        self.frame_11.setStyleSheet("margin: 30px;\n"
                                    "background-color: transparent;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_41 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_41.setMaximumSize(QtCore.QSize(350, 400))
        self.label_41.setStyleSheet("background-color: transparent;")
        self.label_41.setText("")
        self.label_41.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\print.png")))
        self.label_41.setScaledContents(True)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_35.addWidget(self.label_41, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_42 = QtWidgets.QLabel(parent=self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(0, 29, 61);")
        self.label_42.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_35.addWidget(self.label_42)
        self.verticalLayout_24.addWidget(self.frame_11, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_16.addWidget(self.printing_container, 0, 0, 1, 1)
        self.verticalLayout_23.addWidget(self.printing_frame)
        self.stackedWidget.addWidget(self.printing)

    # index 8: Get Photo Page (Veloria)
    def __init_get_photo_page(self):
        # Widget for the whole page
        self.getYourPhoto = QtWidgets.QWidget()
        self.getYourPhoto.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.getYourPhoto.setObjectName("getYourPhoto")
        
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.getYourPhoto)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        
        # Frame with QuickSnap background
        self.get_your_photo = QtWidgets.QFrame(parent=self.getYourPhoto)
        self.get_your_photo.setStyleSheet("#get_your_photo{\n"
                                          "border-image: url('" + resource_path("package\\resource\\img\\main_bg.png").replace("\\", "/") + "');\n"
                                          "}")
        self.get_your_photo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.get_your_photo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.get_your_photo.setObjectName("get_your_photo")
        self.verticalLayout_28.addWidget(self.get_your_photo)
        
        self.gridLayout_21 = QtWidgets.QGridLayout(self.get_your_photo)
        self.gridLayout_21.setObjectName("gridLayout_21")
        
        self.printing_container_2 = QtWidgets.QFrame(parent=self.get_your_photo)
        self.printing_container_2.setMaximumSize(QtCore.QSize(1000, 800))
        self.printing_container_2.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                                "border-radius: 18px;")
        self.printing_container_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.printing_container_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.printing_container_2.setObjectName("printing_container_2")
        self.gridLayout_21.addWidget(self.printing_container_2, 0, 0, 1, 1)
        
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.printing_container_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        
        self.frame_13 = QtWidgets.QFrame(parent=self.printing_container_2)
        self.frame_13.setStyleSheet("background-color: transparent;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_27.addWidget(self.frame_13, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_20.setObjectName("gridLayout_20")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_45 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(0, 29, 61);\n"
                                    "margin: 10px;")
        self.label_45.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_20.addWidget(self.label_45, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        
        # Film Strip Image at center
        self.label_46 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_46.setMaximumSize(QtCore.QSize(500, 600))
        self.label_46.setStyleSheet("background-color: transparent;")
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\photo_strips-removebg-preview.png")))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.gridLayout_20.addWidget(self.label_46, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # "Done" Button at center
        self.done_btn = QtWidgets.QPushButton(parent=self.frame_13)
        self.done_btn.setFont(font)
        self.done_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.done_btn.setStyleSheet("height: 100px;\n"
                                    "width: 100px;\n"
                                    "border: 5px solid rgb(255, 161, 4);\n"
                                    "background-color: rgb(255, 227, 90);\n"
                                    "color: rgb(0, 29, 61);\n"
                                    "border-radius: 50px;")
        self.done_btn.setObjectName("done_btn")
        self.gridLayout_20.addWidget(self.done_btn, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
    
        self.stackedWidget.addWidget(self.getYourPhoto)

    # index ?: Alert Page
    def __init_alert_page(self):
        self.alert = QtWidgets.QWidget()
        self.alert.setObjectName("alert")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.alert)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.alert_frame = QtWidgets.QFrame(parent=self.alert)
        self.alert_frame.setStyleSheet("#alert_frame{\n"
                                       "border-image: url('" + resource_path("package\\resource\\img\\main_bg.png").replace("\\", "/") + "');\n"
                                       "}")
        self.alert_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.alert_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.alert_frame.setObjectName("alert_frame")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.alert_frame)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.alert_container = QtWidgets.QFrame(parent=self.alert_frame)
        self.alert_container.setMaximumSize(QtCore.QSize(1000, 800))
        self.alert_container.setStyleSheet("background-color: rgba(255, 255, 255,0.8);\n"
                                           "border-radius: 18px;")
        self.alert_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.alert_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.alert_container.setObjectName("alert_container")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.alert_container)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_12 = QtWidgets.QFrame(parent=self.alert_container)
        self.frame_12.setStyleSheet("margin: 30px;\n"
                                    "background-color: transparent;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_43 = QtWidgets.QLabel(parent=self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(0, 29, 61);")
        self.label_43.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_19.addWidget(self.label_43, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_44 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_44.setMaximumSize(QtCore.QSize(350, 400))
        self.label_44.setStyleSheet("background-color: transparent;")
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap(resource_path("package\\resource\\img\\danger.png")))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.gridLayout_19.addWidget(self.label_44, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_25.addWidget(self.frame_12)
        self.gridLayout_18.addWidget(self.alert_container, 0, 0, 1, 1)
        self.verticalLayout_26.addWidget(self.alert_frame)
        self.stackedWidget.addWidget(self.alert)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.mainFrame)

    def __init_slots(self):
        # information buttons
        self.btnINFO_intro.clicked.connect(lambda: self.show_popup("Welcome!","Show your index finger and move it to navigate to filters\n\nPinch to select\n\nShow peace sign to capture"))
        self.btnINFO_purpose.clicked.connect(lambda: self.show_popup("Choose!","What package do you want to avail?\n\nIf you are looking for a professional picture, choose the Formal option. It is the great choice for 1x1 and 2x2 photos. \n\nIf you are looking for aesthetic picture, choose the Beauty option."))
        self.btnINFO_gender.clicked.connect(lambda: self.show_popup("Your Gender!","Show your index finger to control the cursor\n\nMove your index to choose\n\nPinch male if you are a boy\n\nPinch female if you are a girl"))
        self.btnINFO_camera.clicked.connect(lambda: self.show_popup("Look at the camera!","Look  directly at the camera\n\nTake a good position\n\nWait for a timer to run to capture your photo"))
        self.btnINFO_filter.clicked.connect(lambda: self.show_popup("Be-you-tify","Look directly at the camera\n\nShow your index to control cursor movements\n\nPinch if you want to choose a filter\n\nMake a peace sign to capture photo"))
        self.btnINFO_style.clicked.connect(lambda: self.show_popup("Choose a package","Show your index to navigate the cursor\n\nYou can choose a different packages\n\nPoint your index to the package that you want to avail\n\nPinch the package to select it"))

        # navigates to capture method
        self.intro_btn_start.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.backGenderButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.backFilterButton.clicked.connect(lambda: self.__handle_camera_back(1))

        # navigates to formal capture: gender selection
        self.btn_Formal.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.backCameraButton.clicked.connect(lambda: self.__handle_camera_back(2))

        # navigates to formal capture
        self.btnMale.clicked.connect(lambda: self.__goto_camera(1, -1, 1))
        self.btnFemale.clicked.connect(lambda: self.__goto_camera(1, -1, 2))
        
        # navigates to beauty capture
        self.btn_Beauty.clicked.connect(lambda: self.__goto_camera(2, print_value=0))
        
        # slots for camera
        self.video_thread.frame_ready.connect(self.__handle_frame)
        self.video_thread.capture_gesture_detected.connect(self.__start_capture_process)
        self.countdown_module.ticked.connect(self.__handle_capture_timer)
        self.countdown_module.finished.connect(self.__navigate_to_capture_result)

        # navigates back to the camera
        self.btn_retake.clicked.connect(self.__return_to_camera)

        # navigates to camera preview
        self.backStyleButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        # navigates to printing
        self.package_A_title.clicked.connect(lambda: self.__handle_package(1))
        self.package_B_title.clicked.connect(lambda: self.__handle_package(2))
        self.package_C_title.clicked.connect(lambda: self.__handle_package(3))
        self.btn_finish.clicked.connect(self.__handle_finish_button)

        # navigates back to start screen
        self.done_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.backPurposeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def show_popup(self, title, content):
        self.window = QtWidgets.QMainWindow()
        self.ui = PopupWidget(title,content)
        self.ui.setupUi(self.window)
        self.ui.btnClose.clicked.connect(lambda: self.window.close())
        self.window.show()

    def __handle_camera_back(self, index):
        self.countdown_module.stop()
        self.video_thread.set_is_capturing(False)
        self.video_thread.background_module.set_background(None)
        self.video_thread.face_module.set_filter_method("null")
        self.video_thread.capture_gesture_detected.connect(self.__start_capture_process)
        self.stackedWidget.setCurrentIndex(index)

    def __start_capture_process(self):
        self.video_thread.capture_gesture_detected.disconnect()
        self.video_thread.set_is_capturing(True)
        self.countdown_module.start()

    def __handle_capture_timer(self, num):
        self.capture_label.setText("" if num == 0 else str(num))

    def __handle_frame(self, frames):
        frame_to_show, self.frame_to_print = frames
        self.camera_label.set_shown_frame(self.camera_label.convert_frame_to_qimage(frame_to_show, self.capture_method_value))
    
    def __handle_filter(self, filter_method, background_path, sticker_path):
        self.video_thread.face_module.set_filter_method(filter_method)
        self.video_thread.face_module.set_filter_path(sticker_path)
        self.video_thread.background_module.set_background(background_path)

    def __navigate_to_capture_result(self):
        self.video_thread.set_mode(0)
        self.video_thread.set_is_capturing(False)
        self.final_image = self.camera_label.convert_frame_to_qimage(self.frame_to_print, self.capture_method_value)
        self.captured_frame_label.setPixmap(QtGui.QPixmap.fromImage(self.final_image))
        self.stackedWidget.setCurrentIndex(5)
        self.video_thread.capture_gesture_detected.connect(self.__start_capture_process)

    def __goto_camera(self, capture_value, print_value, gender_value=-1):
        self.capture_method_value = capture_value
        self.print_method_value = print_value

        if self.capture_method_value == 1:
            self.camera_label = self.camera_formal_label
            self.capture_label = self.capture_formal
            self.gender_value = gender_value
            self.video_thread.formal_module.set_gender(self.gender_value)
            self.capture_label.clicked.connect(self.__start_capture_process)
        elif self.capture_method_value == 2:
            self.camera_label = self.camera_beauty_label
            self.capture_label = self.capture_beauty
            self.capture_label.clicked.connect(self.__start_capture_process)
        
        self.video_thread.set_mode(capture_value)
        self.stackedWidget.setCurrentIndex(capture_value + 2)

    def __return_to_camera(self):
        #self.video_thread.set_mode(self-capture_method_value) wrong
        self.video_thread.set_mode(self.capture_method_value)
        self.stackedWidget.setCurrentIndex(self.capture_method_value + 2)
        self.video_thread.capture_gesture_detected.connect(self.__start_capture_process)

    def __handle_package(self, print_method_value):
        self.print_method_value = print_method_value
        self.__print_image()

    def __handle_finish_button(self):
        self.video_thread.background_module.set_background(None)
        self.video_thread.face_module.set_filter_method("null")

        if self.capture_method_value == 1:
            self.stackedWidget.setCurrentIndex(6)
        elif self.capture_method_value == 2:
            self.print_method_value = 0
            self.__print_image()

    def __print_image(self):
        self.__go_outside_camera_scope(7)
        self.print_module.print(self.final_image, self.print_method_value)
        self.stackedWidget.setCurrentIndex(8)

    def __go_outside_camera_scope(self, index):
        self.capture_method_value = 0
        self.video_thread.set_mode(self.capture_method_value)
        self.stackedWidget.setCurrentIndex(index)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Snap"))
        self.intro_lbl_tagline.setText(_translate("MainWindow", "Picture perfect moments with QuickSnap"))
        self.label_101.setText(_translate("MainWindow", "(Raise your index finger to navigate, and momentarily lower it to select.)"))
        self.intro_btn_start.setText(_translate("MainWindow", "Start QuickSnap"))
        self.btnINFO_intro.setText(_translate("MainWindow", "i"))
        self.label_2.setText(_translate("MainWindow", "Formal"))
        self.label_3.setText(_translate("MainWindow", "Great for 1x1 and 2x2 photos."))
        self.label_5.setText(_translate("MainWindow", "Beauty"))
        self.label_6.setText(_translate("MainWindow", "Great for selfie and groupie."))
        self.btnINFO_purpose.setText(_translate("MainWindow", "i"))
        self.label_103.setText(_translate("MainWindow", "Male"))
        self.label_105.setText(_translate("MainWindow", "Female"))
        self.btnINFO_gender.setText(_translate("MainWindow", "i"))
        self.btnINFO_style.setText(_translate("MainWindow", "i"))
        self.btnINFO_camera.setText(_translate("MainWindow", "i"))
        self.label_10.setText(_translate("MainWindow", "Filters"))
        self.btnINFO_filter.setText(_translate("MainWindow", "i"))
        self.btn_retake.setText(_translate("MainWindow", "Retake"))
        self.btn_finish.setText(_translate("MainWindow", "Finish"))
        self.package_A_title.setText(_translate("MainWindow", "Package A : 8 pcs 1x1 photos"))
        self.package_B_title.setText(_translate("MainWindow", "Package B : 4 pcs 2x2 photos"))
        self.package_C_title.setText(_translate("MainWindow", "Combo : 4 pcs 1x1 & 2 pc 2x2 photos"))
        self.label_42.setText(_translate("MainWindow", "Printing please wait ..."))
        self.label_45.setText(_translate("MainWindow", "Please get your photo."))
        self.done_btn.setText(_translate("MainWindow", "Done"))
        self.label_43.setText(_translate("MainWindow", "Photo paper or ink may running low!"))

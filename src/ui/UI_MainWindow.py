# Form implementation generated from reading ui file '.\src\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.central_widget = QtWidgets.QWidget(parent=MainWindow)
        self.central_widget.setEnabled(True)
        self.central_widget.setMinimumSize(QtCore.QSize(0, 400))
        self.central_widget.setObjectName("central_widget")
        self.tab_main = QtWidgets.QTabWidget(parent=self.central_widget)
        self.tab_main.setEnabled(True)
        self.tab_main.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.tab_main.setMinimumSize(QtCore.QSize(500, 400))
        self.tab_main.setMaximumSize(QtCore.QSize(500, 400))
        self.tab_main.setDocumentMode(False)
        self.tab_main.setTabsClosable(False)
        self.tab_main.setMovable(False)
        self.tab_main.setTabBarAutoHide(False)
        self.tab_main.setObjectName("tab_main")
        self.tab_login = QtWidgets.QWidget()
        self.tab_login.setEnabled(False)
        self.tab_login.setObjectName("tab_login")
        self.lab_login_img = QtWidgets.QLabel(parent=self.tab_login)
        self.lab_login_img.setGeometry(QtCore.QRect(30, 30, 300, 300))
        self.lab_login_img.setText("")
        self.lab_login_img.setObjectName("lab_login_img")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab_login)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 60, 131, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vl_login = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vl_login.setContentsMargins(0, 0, 0, 0)
        self.vl_login.setObjectName("vl_login")
        self.lab_login_info = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lab_login_info.setObjectName("lab_login_info")
        self.vl_login.addWidget(self.lab_login_info)
        self.btn_img_refresh = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_img_refresh.setObjectName("btn_img_refresh")
        self.vl_login.addWidget(self.btn_img_refresh)
        self.btn_logout = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_logout.setObjectName("btn_logout")
        self.vl_login.addWidget(self.btn_logout)
        self.tab_main.addTab(self.tab_login, "")
        self.tab_startup = QtWidgets.QWidget()
        self.tab_startup.setObjectName("tab_startup")
        self.gb_startup = QtWidgets.QGroupBox(parent=self.tab_startup)
        self.gb_startup.setGeometry(QtCore.QRect(10, 130, 471, 231))
        self.gb_startup.setObjectName("gb_startup")
        self.list_startup = QtWidgets.QListWidget(parent=self.gb_startup)
        self.list_startup.setGeometry(QtCore.QRect(11, 31, 171, 191))
        self.list_startup.setObjectName("list_startup")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.gb_startup)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 30, 82, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.vl_startup_btn = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.vl_startup_btn.setContentsMargins(0, 0, 0, 0)
        self.vl_startup_btn.setObjectName("vl_startup_btn")
        self.btn_set_startup = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_set_startup.setObjectName("btn_set_startup")
        self.vl_startup_btn.addWidget(self.btn_set_startup)
        self.btn_unset_startup = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_unset_startup.setObjectName("btn_unset_startup")
        self.vl_startup_btn.addWidget(self.btn_unset_startup)
        self.btn_add_startup = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_add_startup.setObjectName("btn_add_startup")
        self.vl_startup_btn.addWidget(self.btn_add_startup)
        self.btn_del_startup = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_del_startup.setObjectName("btn_del_startup")
        self.vl_startup_btn.addWidget(self.btn_del_startup)
        self.gb_game_path = QtWidgets.QGroupBox(parent=self.tab_startup)
        self.gb_game_path.setGeometry(QtCore.QRect(10, 10, 471, 111))
        self.gb_game_path.setObjectName("gb_game_path")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.gb_game_path)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 80, 174, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.hl_game_path_btn = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.hl_game_path_btn.setContentsMargins(0, 0, 0, 0)
        self.hl_game_path_btn.setObjectName("hl_game_path_btn")
        self.btn_auto_game_path = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.btn_auto_game_path.setObjectName("btn_auto_game_path")
        self.hl_game_path_btn.addWidget(self.btn_auto_game_path)
        self.btn_set_game_path = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.btn_set_game_path.setObjectName("btn_set_game_path")
        self.hl_game_path_btn.addWidget(self.btn_set_game_path)
        self.lab_game_path = QtWidgets.QLabel(parent=self.gb_game_path)
        self.lab_game_path.setGeometry(QtCore.QRect(11, 31, 441, 41))
        self.lab_game_path.setObjectName("lab_game_path")
        self.tab_main.addTab(self.tab_startup, "")
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        self.tab_main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_login_info.setText(_translate("MainWindow", "账号信息:未登录"))
        self.btn_img_refresh.setText(_translate("MainWindow", "刷新二维码"))
        self.btn_logout.setText(_translate("MainWindow", "注销登录"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_login), _translate("MainWindow", "登录"))
        self.gb_startup.setTitle(_translate("MainWindow", "战局锁"))
        self.btn_set_startup.setText(_translate("MainWindow", "设置战局锁"))
        self.btn_unset_startup.setText(_translate("MainWindow", "取消战局锁"))
        self.btn_add_startup.setText(_translate("MainWindow", "新增战局锁"))
        self.btn_del_startup.setText(_translate("MainWindow", "删除战局锁"))
        self.gb_game_path.setTitle(_translate("MainWindow", "GTAV路径"))
        self.btn_auto_game_path.setText(_translate("MainWindow", "自动获取路径"))
        self.btn_set_game_path.setText(_translate("MainWindow", "设置GTAV路径"))
        self.lab_game_path.setText(_translate("MainWindow", "安装路径: 未设置"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_startup), _translate("MainWindow", "战局锁设置"))
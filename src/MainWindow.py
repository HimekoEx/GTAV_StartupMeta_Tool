import sys
from pathlib import Path

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QMessageBox

from DialogAddStartup import DialogAddStartup
from StartupManager import StartupManager
from src.AutoFindGTAVInstallFolder import AutoFindGTAVInstallFolder
from ui.UI_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.manager = StartupManager()

        self.setupUi(self)
        self.initUI()

    # noinspection PyUnresolvedReferences,SpellCheckingInspection
    def initUI(self):
        self.setWindowTitle('GTAOL 战局锁')
        ico_path = Path(__file__).parent / 'res' / 'icon_128.ico'
        self.setWindowIcon(QIcon(str(ico_path.resolve())))

        # 添加任务栏图标
        try:
            from ctypes import windll
            appid = 'mycompany.myproduct.subproduct.version'
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
        except ImportError:
            pass

        # 路径设置按钮事件
        self.btn_auto_game_path.clicked.connect(self.game_path_auto_find)
        self.btn_set_game_path.clicked.connect(self.game_path_set)

        # 启动项设置按钮事件
        self.btn_set_startup.clicked.connect(self.startup_set)
        self.btn_unset_startup.clicked.connect(self.startup_unset)
        self.btn_add_startup.clicked.connect(self.startup_add)
        self.btn_del_startup.clicked.connect(self.startup_del)

        # 加载GTAV路径
        self.game_path_auto_find()

        # 加载启动项
        self.update_startup_list()

    def game_path_auto_find(self):
        """
        自动查找GTAV安装路径

        :return:
        """
        # 优先读取配置文件中的路径
        folder_path = self.manager.get_install_folder()
        if folder_path:
            self.lab_game_path.setText('安装路径: ' + folder_path)
            return

        # 获取steam版的GTAV安装路径
        install_folder = AutoFindGTAVInstallFolder.get_steam_ver()
        if install_folder:
            self.manager.set_install_folder(install_folder)
            self.lab_game_path.setText('安装路径: ' + install_folder)
            return

        QMessageBox.critical(self, '错误', '未找到GTAV安装路径')

    def game_path_set(self):
        """
        设置GTAV安装路径

        :return:
        """
        default_path = QDir.homePath()
        folder_path = QFileDialog(self).getExistingDirectory(
            self, '请选择GTAV安装路径', default_path)
        if folder_path:
            self.manager.set_install_folder(folder_path)
            self.lab_game_path.setText('安装路径: ' + folder_path)

    # noinspection PyBroadException
    def startup_set(self):
        """
        写出当前选中的战局锁文件

        :return:
        """
        selected_items = self.list_startup.selectedItems()
        if not selected_items:
            QMessageBox.information(self, '提示', '未选择战局锁')
            return

        nickname = selected_items[0].text()
        try:
            self.manager.write_startup_meta_file(nickname)
            QMessageBox.information(self, '提示', '战局锁已设置\n请重启GTAV')
        except RuntimeError as e:
            QMessageBox.critical(self, '错误', str(e))
        except Exception:
            QMessageBox.critical(self, '错误', '战局锁设置失败')

    def startup_unset(self):
        """
        删除现有的战局锁文件

        :return:
        """
        self.manager.delete_startup_meta_file()
        QMessageBox.information(self, '提示', '战局锁已删除')

    def startup_add(self):
        """
        添加战局锁(对话框)

        :return:
        """
        dlg = DialogAddStartup()
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return

        nickname = dlg.get_nickname()
        passwd1 = dlg.get_passwd1()
        passwd2 = dlg.get_passwd2()
        self.manager.add_startup_meta(nickname, passwd1, passwd2)
        self.update_startup_list()

    def startup_del(self):
        """
        删除列表中选中的战局锁

        :return:
        """
        selected_items = self.list_startup.selectedItems()
        if not selected_items:
            return

        nickname = selected_items[0].text()
        self.manager.remove_startup_meta(nickname)
        self.update_startup_list()

    def update_startup_list(self):
        """
        更新战局锁列表

        :return:
        """
        self.list_startup.clear()
        self.list_startup.addItems(self.manager.get_startup_list())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

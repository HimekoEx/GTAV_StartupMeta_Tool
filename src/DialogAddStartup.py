from pathlib import Path

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QIcon
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox

from StartupManager import StartupManager
from ui.UI_DialogAddStartup import Ui_DialogAddStartup


class DialogAddStartup(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogAddStartup()
        self.ui.setupUi(self)

        # 设置窗口标题
        self.setWindowTitle('添加战局锁')
        ico_path = Path(__file__).parent / 'res' / 'icon_128.ico'
        self.setWindowIcon(QIcon(str(ico_path.resolve())))

        # 必填项校验
        self.ui.btn_box.accepted.connect(self.validate_and_accept)

        # 文件导入按钮
        self.ui.btn_add_file_path.clicked.connect(self.add_file_path)

        # 启用拖放功能
        self.setAcceptDrops(True)

    def get_nickname(self) -> str:
        """
        获取昵称

        :return: 昵称
        """
        return self.ui.edit_nickname.text()

    def get_passwd1(self) -> str:
        """
        获取密码1

        :return: 密码1
        """
        return self.ui.edit_passwd1.text()

    def get_passwd2(self) -> str:
        """
        获取密码2, 如果为空则返回密码1

        :return: 密码2
        """
        passwd2 = self.ui.edit_passwd2.text()
        return passwd2 if passwd2 else self.get_passwd1()

    def validate_and_accept(self):
        """
        校验必填项并接受对话框

        :return:
        """
        if not self.get_nickname():
            self.ui.edit_nickname.setFocus()
            return
        if not self.get_passwd1():
            self.ui.edit_passwd1.setFocus()
            return
        self.accept()

    # noinspection PyBroadException
    def process_file(self, path: str):
        """
        处理并解析导入的文件

        :param path: 文件路径
        :return:
        """
        try:
            p1, p2 = StartupManager.paser_startup_file(path)
            self.ui.edit_passwd1.setText(p1)
            self.ui.edit_passwd2.setText(p2)

            self.ui.edit_file_path.setText(path)
        except RuntimeError as e:
            QMessageBox.critical(self, '错误', str(e))
        except Exception:
            QMessageBox.critical(self, '错误', f'文件解析失败\n{path}')

    def add_file_path(self):
        """
        导入文件按钮逻辑

        :return:
        """
        default_path = QDir.homePath()
        file_path, _ = QFileDialog.getOpenFileName(
            self, '请选择战局锁文件', default_path, 'All Files (*)')

        if file_path:
            self.process_file(file_path)

    def dragEnterEvent(self, event: QDragEnterEvent):
        """
        拖拽进入窗口事件

        :param event: 事件
        :return:
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """
        拖拽文件释放事件

        :param event: 事件
        :return:
        """
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            file_path = mime_data.urls()[0].toLocalFile()
            self.process_file(file_path)

        event.acceptProposedAction()

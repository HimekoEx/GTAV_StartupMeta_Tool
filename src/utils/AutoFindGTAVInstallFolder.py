import string
import winreg
from pathlib import Path


class AutoFindGTAVInstallFolder:

    @staticmethod
    def find_steam_libraries():
        """
        查找所有Steam存储库路径

        :return: Steam存储库路径列表
        """
        steam_libraries = []
        try:
            # 打开注册表
            key = winreg.HKEY_CURRENT_USER
            reg = winreg.ConnectRegistry(None, key)
            # 打开Steam的注册表项
            sub_key = r"Software\Valve\Steam"
            key = winreg.OpenKey(reg, sub_key)
            # 读取InstallPath值
            sub_name = 'SteamPath'
            install_path = winreg.QueryValueEx(key, sub_name)[0]
            steam_libraries.append(Path(install_path))
        except FileNotFoundError:
            pass

        # 获取所有硬盘根目录
        drives = ['%s:' % d for d in string.ascii_uppercase]
        for drive in drives:
            steam_library = Path(drive) / 'SteamLibrary'
            if steam_library.exists():
                steam_libraries.append(steam_library)

        return steam_libraries

    # noinspection SpellCheckingInspection
    @staticmethod
    def get_steam_ver() -> str:
        """
        获取Steam版GTAV安装路径

        :return: GTAV安装路径
        """
        # 获取steam的所有存储库路径
        steam_libraries = AutoFindGTAVInstallFolder.find_steam_libraries()

        # 查找GTAV安装路径
        for steam_library in steam_libraries:
            common_folder = steam_library / 'steamapps' / 'common'
            gtav_install_folder = common_folder / 'Grand Theft Auto V'
            if gtav_install_folder.exists():
                return str(gtav_install_folder.resolve())

        return None

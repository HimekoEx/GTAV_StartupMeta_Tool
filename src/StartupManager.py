import re
from pathlib import Path

from ConfigManager import ConfigManager

# source: https://github.com/Raitou/GTA-V-Public-Solo-Friend-Session/blob/main/startup.meta
# noinspection SpellCheckingInspection
_BASE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<!--%PASSWORD1%-->
<CDataFileMgr__ContentsOfDataFileXml>
	<disabledFiles />
	<includedXmlFiles itemType="CDataFileMgr__DataFileArray" />
	<includedDataFiles />
	<dataFiles itemType="CDataFileMgr__DataFile">
	  <Item>
	   <filename>platform:/data/cdimages/scaleform_platform_pc.rpf</filename>
	   <fileType>RPF_FILE</fileType>
	  </Item>
	  <Item>
	   <filename>platform:/data/cdimages/scaleform_frontend.rpf</filename>
	   <fileType>RPF_FILE_PRE_INSTALL</fileType>
	  </Item>
	 </dataFiles>
	<contentChangeSets itemType="CDataFileMgr__ContentChangeSet" />
	<dataFiles itemType="CDataFileMgr__DataFile" />
	<patchFiles />
</CDataFileMgr__ContentsOfDataFileXml>                     
<!--%PASSWORD2%-->"""


class StartupManager:

    def __init__(self):
        self.config_manager = ConfigManager()

    def get_install_folder(self) -> str:
        """
        获取GTAV安装路径

        :return: GTAV安装路径
        """
        return self.config_manager.get_str_value("GTAV_InstallFolder")

    def set_install_folder(self, install_folder: str):
        """
        设置GTAV安装路径

        :param install_folder: GTAV安装路径
        :return:
        """
        self.config_manager.set_str_value("GTAV_InstallFolder", install_folder)
        self.config_manager.save_config()

    def get_startup_path(self) -> Path:
        """
        获取`startup.meta`文件路径

        :return: `startup.meta`文件路径
        """
        install_folder = self.get_install_folder()
        if install_folder:
            startup_meta_path = Path(install_folder) / 'x64' / 'data' / 'startup.meta'
            startup_meta_path.parent.mkdir(parents=True, exist_ok=True)
            return startup_meta_path
        else:
            return None

    def write_startup_meta(self, nickname: str):
        """
        写入`startup.meta`文件

        :param nickname: 启动项名称
        :return:
        """
        startup_meta_path = self.get_startup_path()
        if startup_meta_path is not None:
            passwd1, passwd2 = self.get_startup_meta().get(nickname)
            if passwd1 and passwd2:
                file_content = _BASE_XML \
                    .replace('%PASSWORD1%', passwd1) \
                    .replace('%PASSWORD2%', passwd2)
                startup_meta_path.write_text(file_content, encoding='utf-8')
            else:
                raise RuntimeError(f"战局锁不存在: [{nickname}]")
        else:
            raise RuntimeError("GTAV安装路径未设置")

    def delete_startup_meta_path(self):
        """
        删除startup.meta文件

        :return:
        """
        startup_meta_path = self.get_startup_path()
        if startup_meta_path is not None and startup_meta_path.exists():
            startup_meta_path.unlink()

    def get_startup_meta(self) -> dict:
        """
        获取启动项

        :return: 启动项
        """
        return self.config_manager.get_dict_value("StartupMeta", {})

    def get_startup_list(self) -> list:
        """
        获取启动项列表

        :return: 启动项列表
        """
        return list(self.get_startup_meta().keys())

    def set_startup_meta(self, startup_meta: dict):
        """
        设置启动项

        :param startup_meta: 启动项
        :return:
        """
        self.config_manager.set_dict_value("StartupMeta", startup_meta)
        self.config_manager.save_config()

    def add_startup_meta(self, nickname: str, passwd1: str, passwd2: str):
        """
        添加启动项

        :param nickname: 启动项名称
        :param passwd1: 启动项密码1
        :param passwd2: 启动项密码2
        :return:
        """
        startup_meta = self.get_startup_meta()
        startup_meta[nickname] = (passwd1, passwd2)
        self.set_startup_meta(startup_meta)

    def remove_startup_meta(self, nickname: str) -> dict:
        """
        删除启动项

        :param nickname: 启动项名称
        :return: 启动项
        """
        startup_meta = self.get_startup_meta()
        if nickname in startup_meta.keys():
            del startup_meta[nickname]
            self.set_startup_meta(startup_meta)
            return startup_meta
        else:
            raise RuntimeError(f"战局锁不存在:\n[{nickname}]")

    @staticmethod
    def paser_startup_file(path: str):
        """
        解析文件内容, 并添加启动项

        :param path: 文件路径
        :return:
        """

        # 输入的是文件路径, 提取密码
        file_path = Path(path.replace('"', '').strip())
        if not file_path.exists():
            raise RuntimeError(f"文件不存在:\n{file_path}")

        file_content = file_path.read_text(encoding='utf-8')
        matches = re.findall(r'<!--(.*?)-->', file_content)
        if matches is not None and len(matches) == 2:
            passwd1, passwd2 = matches
            return passwd1, passwd2
        else:
            raise RuntimeError(f"文件识别失败:\n{file_path}")

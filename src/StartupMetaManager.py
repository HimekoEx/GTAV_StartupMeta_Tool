import re
from pathlib import Path

from ConfigManager import ConfigManager

# noinspection SpellCheckingInspection
# source: https://github.com/Raitou/GTA-V-Public-Solo-Friend-Session/blob/main/startup.meta
_BASE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<!--%PASSWORD%-->
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
<!--%PASSWORD%-->"""


# noinspection SpellCheckingInspection
class StartupMetaManager:
    def __init__(self):
        self.config_manager = ConfigManager()

    def get_install_folder(self) -> str:
        """
        获取GTAV安装目录

        :return: GTAV安装目录
        """
        return self.config_manager.get_str_value("GTAV", "InstallFolder")

    def set_install_folder(self, install_folder: str):
        """
        设置GTAV安装目录

        :param install_folder: GTAV安装目录
        :return:
        """
        self.config_manager.set_str_value("GTAV", "InstallFolder", install_folder)
        self.config_manager.save()

    def get_startup_meta_path(self) -> Path:
        """
        获取startup.meta文件路径

        :return: startup.meta文件路径
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
        写入startup.meta文件

        :param nickname: 启动项名称
        :return:
        """
        startup_meta_path = self.get_startup_meta_path()
        if startup_meta_path is not None:
            passwd = self.get_startup_meta().get(nickname)
            if passwd is not None:
                file_content = _BASE_XML.replace('%PASSWORD%', passwd)
                startup_meta_path.write_text(file_content, encoding='utf-8')
            else:
                raise Exception(f"启动项不存在: [{nickname}]")
        else:
            raise Exception("GTAV安装目录未设置")

    def delete_startup_meta_path(self):
        """
        删除startup.meta文件

        :return:
        """
        startup_meta_path = self.get_startup_meta_path()
        if startup_meta_path is not None and startup_meta_path.exists():
            startup_meta_path.unlink()

    def get_startup_meta(self) -> dict:
        """
        获取启动项

        :return: 启动项
        """
        return self.config_manager.get_dict_value("StartupMeta", {})

    def set_startup_meta(self, startup_meta: dict):
        """
        设置启动项

        :param startup_meta: 启动项
        :return:
        """
        self.config_manager.set_dict_value("StartupMeta", startup_meta)
        self.config_manager.save()

    def add_startup_meta(self, nickname: str, passwd: str):
        """
        添加启动项

        :param nickname: 启动项名称
        :param passwd: 启动项密码
        :return:
        """
        startup_meta = self.get_startup_meta()
        startup_meta[nickname] = passwd
        self.set_startup_meta(startup_meta)

    def remove_startup_meta(self, nickname: str) -> dict:
        """
        删除启动项

        :param nickname: 启动项名称
        :return: 启动项
        """
        startup_meta = self.get_startup_meta()
        if nickname in startup_meta:
            del startup_meta[nickname]
            self.config_manager.remove_dict_value("StartupMeta", nickname)
            self.config_manager.save()
            return startup_meta
        else:
            raise Exception(f"启动项不存在: [{nickname}]")

    def paser_startup_meta_passwd(self, input_str: str, nickname: str):
        """
        解析输入的字符串, 并添加启动项

        :param input_str: 输入字符串
        :param nickname: 启动项名称
        :return:
        """
        if nickname in self.get_startup_meta():
            raise Exception(f"启动项已存在: [{nickname}]")

        if input_str.isdigit():  # 输入的是密码(纯数字?)
            self.add_startup_meta(nickname, input_str)
            return

        # 输入的是文件路径, 提取密码
        file_path = Path(input_str.replace('"', '').strip())
        if not file_path.exists():
            raise Exception(f"文件不存在: {file_path}")

        file_content = file_path.read_text(encoding='utf-8')
        match = re.search(r'<!--(.*?)-->', file_content)
        if match:
            passwd = match.group(1)
            self.add_startup_meta(nickname, passwd)
        else:
            raise Exception(f"文件中未识别到密码: {file_path}")

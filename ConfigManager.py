import configparser
import tempfile
from pathlib import Path


class ConfigManager:
    def __init__(self, file_path: Path = None):
        if file_path is None:
            file_path = self.get_config_path()
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(file_path.resolve(), encoding='utf-8')

    # noinspection PyMethodMayBeStatic
    def get_config_path(self) -> Path:
        """
        获取Rockstar Games的配置文件路径

        :return: 配置文件路径
        """
        path_local = Path(tempfile.gettempdir()).parent
        path_config = path_local / "Rockstar Games" / "startup_config.ini"
        path_config.parent.mkdir(parents=True, exist_ok=True)
        return path_config

    def save(self):
        """
        保存配置到文件

        :return:
        """
        with open(self.file_path, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def get_str_value(self, section: str, key: str, default: str = None) -> str:
        """
        获取配置项的值

        :param section: 配置项的节
        :param key: 配置项的键
        :param default: 默认值
        :return: 配置项的值
        """
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def set_str_value(self, section: str, key: str, value: str):
        """
        设置配置项的值

        :param section: 配置项的节
        :param key: 配置项的键
        :param value: 配置项的值
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)

    def get_dict_value(self, section: str, default: dict = None) -> dict:
        """
        获取配置项的值

        :param section: 配置项的节
        :param default: 默认值
        :return: 配置项kv对
        """
        try:
            return dict(self.config.items(section))
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def set_dict_value(self, section: str, dictionary: dict):
        """
        设置配置项的值

        :param section: 配置项的节
        :param dictionary: 配置项kv对
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        for k, v in dictionary.items():
            self.config.set(section, k, v)

    def remove_dict_value(self, section: str, key: str):
        """
        删除配置项的值

        :param section: 配置项的节
        :param key: 配置项的键
        """
        self.config.remove_option(section, key)
        if len(self.config.items(section)) == 0:
            self.config.remove_section(section)

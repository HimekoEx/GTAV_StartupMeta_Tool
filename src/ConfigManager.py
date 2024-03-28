import json
import tempfile
from base64 import b64encode, b64decode
from pathlib import Path

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_KEY = b'\xd2\xd9\xed\xdd\xd9\xb2\x16P\x92\xe0\x01Qv/F\x13' \
       b'\r\x92\xe3J\xf9\x89\x06\xd4\xc4\xf9Z9\x80\x1d\xf3\xa4'

_IV = b'\xbc\x1fH\x89L\xe7`8]\xacj\xf3B\xce\xf8\xb7'


class ConfigManager:

    def __init__(self, key: bytes = None, iv: bytes = None, path: Path = None):
        self.file_path = path if path else self.get_config_path()
        self._key = key if key else _KEY
        self._iv = iv if iv else _IV
        self._config = self._load_config()

    def _encrypt(self, plaintext) -> str:
        """
        加密字符串

        :param plaintext: 明文
        :return: 密文
        """
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()
        cipher = Cipher(algorithms.AES(self._key), modes.CBC(self._iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return b64encode(ciphertext).decode()

    # noinspection SpellCheckingInspection
    def _decrypt(self, ciphertext) -> str:
        """
        解密字符串

        :param ciphertext: 密文
        :return: 明文
        """
        cipher = Cipher(algorithms.AES(self._key), modes.CBC(self._iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(decrypted_data) + unpadder.finalize()
        return plaintext.decode()

    @staticmethod
    def get_config_path() -> Path:
        """
        获取`Rockstar Games`的配置文件路径

        :return: 配置文件路径
        """
        path_local = Path(tempfile.gettempdir()).parent
        path_config = path_local / "Rockstar Games" / "GTAOL_SMT.dat"
        path_config.parent.mkdir(parents=True, exist_ok=True)
        return path_config

    def _load_config(self) -> dict:
        """
        从文件中加载配置

        :return: 解密后的配置字典
        """
        if not self.file_path.exists():
            return {}
        with open(self.file_path, 'r') as f:
            encrypted_data = f.read()
        decrypted_data = self._decrypt(encrypted_data)
        return json.loads(decrypted_data)

    def save_config(self):
        """
        保存配置到文件

        :return:
        """
        encrypted_data = self._encrypt(json.dumps(self._config))
        with open(self.file_path, 'w') as f:
            f.write(encrypted_data)

    def get_str_value(self, key: str, default: str = None) -> str:
        """
        获取指定键的字符串值

        :param key: 键名
        :param default: 默认值（如果键不存在）
        :return: 字符串值
        """
        return self._config.get(key, default)

    def set_str_value(self, key: str, value: str):
        """
        设置指定键对应的字符串值

        :param key: 键名
        :param value: 字符串值
        """
        self._config[key] = value

    def get_dict_value(self, key: str, default: dict = None) -> dict:
        """
        获取指定键对应的字典值

        :param key: 键名
        :param default: 默认值（如果键不存在时返回）
        :return: 键对应的字典值，如果键不存在则返回默认值
        """
        return self._config.get(key, default)

    def set_dict_value(self, key: str, value: dict):
        """
        设置指定键对应的字典值

        :param key: 键名
        :param value: 字典值
        """
        self._config[key] = value

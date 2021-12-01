import logging
import os
import sys

import yaml


def getFiles(path):
    '''
    获取目录下所有文件，并通过列表返回
    :param path: 目录
    :return: 所有文件列表
    '''
    files_list = []
    for root, dirs, files in os.walk(path):
        files_list += files
    return files_list


def findFile(file, list):
    '''
    查找file是否在list中，file可以是子串
    :param file: 需要查找的名称，可以是字串
    :param list: 被查找的列表
    :return: bool
    '''
    for l in list:
        if file in l:
            return True
    return False


def pyInstaller(filename):
    os.system('Pyinstaller -F -w {}'.format(filename))


class Assistant:
    __loc = ''
    __log_filename = 'log.txt'
    __config_filename = 'config.yml'

    def __init__(self, ):
        with open(self.__log_filename, 'a', encoding='utf-8') as f:
            f.close()
        self.__loc = sys.path[0]

    def Log(self):
        """
        创建一个日志
        """
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler(self.__log_filename, mode='a', encoding='utf-8')
        fh.setFormatter(logging.Formatter("[%(asctime)s]:%(levelname)s:%(message)s"))
        logger.addHandler(fh)
        return logger

    def readConfig(self):
        try:
            with open(os.path.join(os.getcwd(), self.__config_filename), mode='r', encoding='utf-8') as f:
                yml_data = f.read()
                return yaml.load(yml_data, Loader=yaml.SafeLoader)
        except Exception as e:
            logger.warning(e)


assistant = Assistant()
logger = assistant.Log()
config = assistant.readConfig()

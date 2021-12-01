# -*- encoding=utf-8 -*- #

import os
import platform
import ctypes
import datetime
import psutil
import sys


def get_free_space_mb(folder):
    """
    获取磁盘剩余空间
    :param folder: 磁盘路径 例如 D:\\
    :return: 剩余空间(保留两位小数) 单位 G
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return round(free_bytes.value / 1024 / 1024 / 1024, 2)
    else:
        st = os.statvfs(folder)
        return round(st.f_bavail * st.f_frsize / 1024 / 1024, 2)


def format_output(path, file):
    """
    格式化输出到此文件同目录下，文件名为file
    :param file: 可以包含.txt后缀，也可以不需要
    :return: 无
    """
    if file[-4:] != '.txt':
        file += '.txt'
    with open(os.path.join(path, file), 'a') as f:
        f.write('{}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        for i in range(len(psutil.disk_partitions())):
            now_device = psutil.disk_partitions()[i].device
            now_free_space = get_free_space_mb(psutil.disk_partitions()[i].device)
            file_lines = []
            with open(os.path.join(path, file), 'r') as rf:
                file_lines = rf.readlines()[-5:]
            exchange_space = 0
            for last in file_lines:
                if now_device in last:
                    last_free_space = float(last[last.find(' ') + 1:last.find('G')])
                    exchange_space = round(now_free_space - last_free_space, 2)
            f.write(now_device + ' ' + str(now_free_space) + 'G')
            len_now_free_space = len(str(now_free_space))
            while 10 - len_now_free_space > 0:
                f.write(' ')
                len_now_free_space += 1
            if exchange_space >= 0:
                f.write('+')
            f.write('{:.2f}G\n'.format(exchange_space))


def get_config():
    '''
    读取config文件
    :return config字典
    '''
    config = {}
    with open('{}config'.format(sys.argv[0][:sys.argv[0].rfind('\\') + 1]), 'r') as f:
        data = f.readlines()
        # print(data)
        if not (data[0] == '[start]\n' and (data[-1] == '[end]' or data[-1] == '[end]\n')):
            print('lack [start] or [end]')
            exit(-1)
        data = data[1:-1]
        # print(data)
        for line in data:
            # print(line)
            config[line.split('=')[0]] = line.split('=')[-1][:-1]
    # print(config)
    return config
    
    
if __name__ == '__main__':
    config = get_config()
    # print(config['path'], config['filename'])
    # format_output(r'D:\_Software\_check_disk_free_space','diskinfo')
    format_output(os.getcwd(), config['filename'])
import os
import shutil
import sys

from Assistant import config, logger, pyInstaller


# config['Path']
# config['RemoveFileName']


def remove():
    logger.info('正在删除文件名中的 {} ...'.format(config['RemoveFileName']))
    # print(config['RemoveFileName'])
    # exit(0)
    for root, dirs, files in os.walk(config['Path']):
        for file in files:
            file = os.path.join(root, file)
            logger.info('正在处理 {} ...'.format(file))
            try:
                shutil.move(file, file.replace(config['RemoveFileName'], ''))
            except Exception as e:
                logger.warning(e)
            logger.info('处理成功 {} ...'.format(file))


if __name__ == '__main__':
    remove()
    # os.system('dir')
    # pyInstaller('removeSomeFileName.py')

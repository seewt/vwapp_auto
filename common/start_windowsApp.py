from logconf import logger
import os
import time
from winApp_util import isRunning


def open_winapp(appd_dir,timeout=30):
    '''

    :param appd_dir:传入程序启动路径
    :param timeout: 启动后等待时间
    :return:
    '''
    os.startfile(appd_dir)
    time.sleep(timeout)

if __name__ == '__main__':

    while True:
        result = isRunning('Nox.exe')
        if result==True:
            logger.info('程序已运行')
            break
        else:
            logger.warning('程序未运行')
            appdir = r'D:\Program Files\Nox\bin\Nox.exe'
            open_winapp(appdir)
            continue


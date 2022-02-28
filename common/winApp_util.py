import os
import time


def isRunning(processName):
    '''
    :param processName:
    :return:
    监空 windows程序是否正常运行
    '''

    try:
        print('tasklist | findstr ' + processName)
        process=len(os.popen('tasklist|findstr '+processName).readlines())

        if process >=1:
            time.sleep(3)
            return True
        else:
            return False

    except:
        from common.logconf import logger
        logger.error("安卓模拟器未正常运行，请检查！！！")
        return False
    





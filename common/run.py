import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from winApp_util import isRunning
from start_windowsApp import open_winapp
from adb_connect_Util import adb_connect
from close_winApp_Util import close_app
from mail_text import mt

def excute():
    os.popen('adb shell am start -n com.android.gallery3d/com.android.gallery3d.app.GalleryActivity')
    print(os.system('python vwapp_2.py'))


def run():
    winapp_heart = isRunning('Nox.exe')
    time.sleep(2)
    if winapp_heart:
        if adb_connect('127.0.0.1:62001'):
            excute()
        else:
            from common.logconf import logger
            logger.error('设备未连接，或无法连接成功')
    else:
        open_winapp(r'D:\Program Files\Nox\bin\Nox.exe',timeout=20)
        if adb_connect('127.0.0.1:62001'):
            excute()
        else:
            from common.logconf import logger
            logger.error('设备未连接，或无法连接成功')
            mt.send_mail('设备连接异常','adb连接异常，请检查')

    close_app('Nox.exe')


if __name__ == '__main__':
    # run()
    s1 = BlockingScheduler()
    s1.add_job(run,'cron',hour=9,minute=36)
    s1.start()
import os
import adbutils
from logconf import logger
devices = adbutils.adb
def check_connect():
    global is_connect
    devices_list = devices.device_list()
    if len(devices_list)>=1:
        is_connect = True
        logger.info('已连接到设备%s',devices_list)
    else:
        is_connect = False
    logger.debug('设备是否已经连接：%s',is_connect)
    return is_connect


# def excute_times(num):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             i = 0
#             while  i <num:
#                 func(*args, **kw)
#                 i+=1
#         return wrapper
#     return decorator


def adb_connect(host=None):
    result = check_connect()
    i = 1
    while not result:
        try:
            res=devices.connect(host)
        except TypeError as e:
            logger.error(e)
        result=check_connect()
        logger.debug('第%s次连接结果为%s'%(i,res))
        if i>=2:
            break
        i+=1
        logger.debug('尝试连接的结果为%s',result)
    logger.debug('connect结果返回: %s', result)
    return result




if __name__ == '__main__':
    adb_connect(22222)

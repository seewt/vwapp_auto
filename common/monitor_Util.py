from logconf import logger

# 添加监控
def window_Monitor(obj,onoff=1):
    '''
    :param obj: 传入u2对象
    :param onoff: 1开启监控，0 移除监控
    :return:
    '''

    if onoff ==1:
        obj.d.watcher.when('跳过').click()
        obj.d.watcher.when('同意').click()
        obj.d.watcher.when('忽略此版本').click()
        obj.d.watcher.when('不在提示').click()
        obj.d.watcher.start(2)
        logger.info('创建了弹窗监控')
    else:
        obj.d.watcher.remove()
        logger.info('移除弹窗监控')

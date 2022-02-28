import logging
from logging import PlaceHolder
# 创建一个日志记录器
logger = logging.getLogger('vwlog')

# 设置日志记录器的等级 INFO
logger.setLevel(logging.DEBUG)

# 分别创建于一个输出到本地文件 和 console 的日志处理器
steram_handler = logging.StreamHandler()
file_handler=logging.FileHandler(filename='D:\\auto_task\\log\\vw_app.log',mode='a',encoding='utf-8')


# 设置处理器 输出日志的等级
steram_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# loger.removeHandler()  #接触绑定


# 创建一个日志格式器
formatter = logging.Formatter("%(asctime)s | file: %(pathname)s \n | %(name)s | %(levelname)s | module:  %(module)s | funcName:  %(funcName)s() | line %(lineno)s | %(message)s")

# 设置处理器输出的日志格式
file_handler.setFormatter(formatter)
steram_handler.setFormatter(formatter)


# 设置一个过滤器
# fl1 = logging.Filter('app2log')

# 给日志记录器设置一个过滤器 ,(从根部开始过滤)
# loger.addFilter(fl1)


#还可以给 handler 设置过滤器 (在输出的时候过滤)
# steram_handler.addFilter(fl1)


# 记录器设置一个处理器
logger.addHandler(steram_handler)
logger.addHandler(file_handler)

# 写入日志
# loger.debug('debug log')
# loger.info('info log')
# loger.warning('warning log')
# loger.error('error log')
# loger.critical('critical log')

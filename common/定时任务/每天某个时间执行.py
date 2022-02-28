from apscheduler.schedulers.blocking import BlockingScheduler
from random import randint

def myjob():
    print('hhhhh')

s1 = BlockingScheduler()
s1.add_job(myjob,'cron',hour=22,minute=16)
s1.start()
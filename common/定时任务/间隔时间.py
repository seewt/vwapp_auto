import time,datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from random import  randint

def myjob():
    print(datetime.datetime.now())


s1 = BlockingScheduler()
s1.add_job(myjob,'interval',seconds=5)
s1.start()
import datetime
from random import randint
from song_Util import getSong
from day_sentence_Util import get_sentence
from logconf import logger

def get_content():

     num = randint(0,299)
     songName,singer = getSong(num)
     nowtime=datetime.datetime.now().strftime('%Y-%m-%d')
     text = get_sentence()
     body = [['云村音乐大赏','今日音乐推荐'+'《'+songName+'》','云村音乐-今日推荐由'+'\"'+singer+'\" 演唱的'+'《'+songName+'》'],
     ['双周早起打卡挑战',nowtime+' 今日份打卡',text]]
     # ['晒图赚积分 互助赢好礼','晒图赚积分 互助赢好礼',nowtime+'晒图赚积分 互助赢好礼']]
     # ['《追雪人》追综日记','堆了个雪人','由于雪人太小，被鸭子吃掉了']]

     logger.info(body)
     return body

if __name__ == '__main__':
     content = get_content()
     # print(content)
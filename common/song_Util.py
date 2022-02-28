import requests,json
import jsonpath

from random import  randint

def getSong(data):
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?topid=26&platform=yqq.json&jsonpCallback=MusicJsonCallbacktoplist'

    res = requests.request('get', url).text
    res1 = res.split('MusicJsonCallbacktoplist')

    res2 = res1[1]
    num = len(res2) - 1
    res3 = res2[1:num]
    res4 = json.loads(res3)
    soneNames = jsonpath.jsonpath(res4, '$..songname')
    singers = jsonpath.jsonpath(res4, '$..singer')
    return soneNames[data],singers[data][0]['name']


if __name__ == '__main__':
    num = randint(0,300)
    getSong(num)
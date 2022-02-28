import requests
import jsonpath,os
from logconf import logger


# adb push D:\auto_task\excute_image\pic.png /sdcard/Pictures

def get_sentence():
    url = 'https://apier.youngam.cn/essay/one'
    headers = {'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    res = requests.request('get',url,headers=headers).json()
    text = jsonpath.jsonpath(res,'$..dataList')[0][0]
    sentence = text['text']
    pic_url = text['src']
    pic_path = os.getcwd().split('common')[0]+'excute_image\\pic.png'
    pic_src = requests.request('get',pic_url).content
    with open(pic_path,'wb') as f:
        f.write(pic_src)
    os.popen(r'adb push D:\auto_task\excute_image\pic.png /sdcard/Pictures')
    # logger.info(cmd_res.read())
    # print(os.system(r'adb push D:\auto_task\excute_image\pic.png /sdcard/Pictures'))
    return sentence
if __name__ == '__main__':
    get_sentence()
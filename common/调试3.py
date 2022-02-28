import uiautomator2 as u2
import adbutils

from common.adb_connect_Util import adb_connect
adb_connect('127.0.0.1:52001')

device_serNo = adbutils.adb.device_list()[0].serial
print(device_serNo)
d = u2.connect(device_serNo)
d.swipe_ext('up',1.0)
d.swipe()

# from mail_picture import m,image
# m.send_mail(image)

# jd = d.xpath('//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/daily_clock_on_novice_tasks_list2"]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]').info['text']
# task_no = int(jd.split('/')[0])
# task_content = body[task_no]
#
#
# content = body[task_no]
# text = content[0]
# title = content[1]
# main_body = content[2]
#
#
# print(text,title,main_body)
#
#
# # 点击去完成
# d.xpath('//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/daily_clock_on_novice_tasks_list2"]/android.view.ViewGroup[1]/android.widget.TextView[1]').click_exists()
# # 点击添加主题
# d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/tv_theme").click()
# d(text='选择主题').wait()
# time.sleep(1)
# d.swipe_ext("up", 0.8)
# d(text=text).wait()
#
# # d.watcher.when('云村音乐大赏').click()
# d(text=text).click_exists()
# # d.watcher.start()
# # d.watcher.remove
#
# # 选中标题
# d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/new_bbs_title_edit").click()
# d.set_fastinput_ime(True)
# d.send_keys(title)
# # 选中内容
# d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/rich_editor_item_edit_text").click()
# d.send_keys(main_body)
# d.set_fastinput_ime(False)


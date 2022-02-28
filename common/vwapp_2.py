import datetime
from random import randint
from logconf import logger
import uiautomator2 as u2
import time
import adbutils
from monitor_Util import window_Monitor
from content_Util import get_content
from mail_picture import mp
from mail_text import mt

class autoScore:
    # init 方法的第一个参数永远是 self,表示创建实例的本身，
    def __init__(self,d):       #绑定实例属性
        self.d=d
        print(self.d.device_info)
    # 启动app
    def start(self):
        self.d.app_start("com.timanetworks.android.faw.vw.aftermarket.release", stop=True)

    # 点击进入我的页面
    def mypage(self):
        # 等待我的入口出现
        self.d(text='我的').wait()
        # 点击我的
        self.d.xpath(
            '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/user_item"]/android.widget.ImageView[1]').click()

    # 进入任务中心页，并且获取任务进度
    def get_task(self):
        time.sleep(2)
        try:
            d(text='任务中心').wait()
            # 点击任务中心
            self.d(text="任务中心").click()
            self.d(text='每日签到').wait()
            # 向上滑动80%
            self.d.swipe_ext("up", 0.6)
            # 等待日常任务出现
            self.d(text='社区圈子发帖').wait()
            # 检查当前任务进度
            task1 = self.d(text='2/5 +3积分').exists
            task3 = self.d(text='8/8 +1积分').exists
            jd = d.xpath(
                '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/daily_clock_on_novice_tasks_list2"]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]').info[
                'text']
            task1_no = int(jd.split('/')[0])
            return task1, task3, task1_no
        except Exception as e:
            logger.error(e)
            mt.send_mail('任务进度获取异常','执行任务异常')




    # 任务中心页面。选择指定任务
    def task_center(self):
        # 获取任务进度
        task1,task3,task1_no= self.get_task()
        logger.info('开始执行任务1')
        while not task1:
            # 点击 社区发帖 去完成按钮
            self.d.xpath(
                '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/daily_clock_on_novice_tasks_list2"]/android.view.ViewGroup[1]/android.widget.TextView[1]').click_exists()
            self.post_content(task1_no)
            task1, task3,task1_no = self.get_task()

        logger.info('开始执行任务3')
        while not task3:
            # 点击进入任务3
            self.d.xpath('//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/daily_clock_on_novice_tasks_list2"]/android.view.ViewGroup[3]/android.widget.TextView[1]').click()
            # 选中第一个帖子
            self.d.xpath('//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/base_swipe_list"]/android.widget.LinearLayout[1]').click()
            self.comment()
            time.sleep(1)
            # 点击返回
            self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/action_bar_back_icon").click()
            self.mypage()
            task1, task3,task1_no= self.get_task()
        image = "D:\\auto_task\\excute_image\\1.jpg"
        self.d(text='日常任务').wait()
        self.d.screenshot(image)
        mp.send_mail(image)
        logger.info('日常任务已经完成')


    # 编写帖子内容，并发布
    def post_content(self,task_no):
        content = get_content()[task_no]
        text = content[0]
        title = content[1]
        main_body = content[2]
        # 添加主题
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/tv_theme").click()
        self.d(text='选择主题').wait()
        time.sleep(2)
        # 向上滑动80%
        self.d.swipe(0.582, 0.979,0.582, 0.103,0.1)
        time.sleep(2)
        self.d(text=text).wait()
        # 选择双周打卡
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/circle_topic_item_name_txt",
          text=text).click()

        # 选中标题
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/new_bbs_title_edit").click()
        self.d.set_fastinput_ime(True)
        self.d.send_keys(title)
        # 选中内容
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/rich_editor_item_edit_text").click()
        self.d.send_keys(main_body)
        self.d.set_fastinput_ime(False)

        time.sleep(1)
        # self.d.click(0.579, 0.514)
        self.d.click(0.054, 0.975)
        # 选中图片
        time.sleep(1)
        # 从相册选取
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/pw_text", text="从手机相册选择").click()
        time.sleep(1)
        # 随机选取相册图片
        num = str(randint(1, 2))
        self.d.xpath(
            '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/recyclerview"]/android.widget.FrameLayout[' + num + ']/android.view.View[1]').click()
        # 点击使用
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/button_apply").click()
        self.d.set_fastinput_ime(False)
        # 点击发布
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/top_action_bar_right_text").click()

    # 进行评论
    def comment(self):
        self.d(text='详情').wait()
        self.d(text='我也来说一句...').wait()
        # 选中评论输入框
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/write_comment_bar").click()
        self.d.set_fastinput_ime(True)
        self.d.send_keys("顶楼主")
        self.d.set_fastinput_ime(False)
        # 发布评论
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/comment_publish_btn").click()

    def run(self):
        self.start()
        window_Monitor(self)
        self.mypage()
        self.task_center()
        window_Monitor(self,0)

# 常用命令
# d(text="收益明细").exists    检索页面是否有收益明细 并返回布尔值
# d(text="收益明细").info       获取ui对象信息
# d(text="提现记录").click()    点击
# d(text="银行卡已到账").count     统计相同条件的数目
# d.swipe(0.107, 0.936, 0.176, 0.179)    向上滑动 参数为坐标
# d.double_click(0.847, 0.061)      对指定坐标 进行双击操作

if __name__ == '__main__':
    device_serNo = adbutils.adb.device_list()[0].serial
    logger.info('自动化脚本设备连接信息%s',device_serNo)
    d = u2.connect(device_serNo)
    a = autoScore(d)
    a.run()











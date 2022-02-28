import datetime
import uiautomator2 as u2
import time
import adbutils

class autoScore:
    # init 方法的第一个参数永远是 self,表示创建实例的本身，
    def __init__(self,d):       #绑定实例属性
        self.d=d
        print(self.d.device_info)
    # 启动app
    def start(self):
        self.d.app_start("com.timanetworks.android.faw.vw.aftermarket.release", stop=True)

    # 添加监控
    def addmonitor(self):
        self.d.watcher.when('跳过').click()
        self.d.watcher.when('同意').click()
        self.d.watcher.when('忽略此版本').click()
        self.d.watcher.when('不在提示').click()
        self.d.watcher.start(2)
    # 移除所有监控
    def delmonitor(self):
        self.d.watcher.remove()


    # 点击进入我的页面
    def mypage(self):
        # 等待我的入口出现
        self.d(text='我的').wait()
        # 点击我的
        self.d.xpath(
            '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/user_item"]/android.widget.ImageView[1]').click()

    # 进入任务中心页，并且获取任务进度
    def get_task(self):
        # 点击任务中心
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/tv_menu", text="任务中心").click()
        self.d(text='每日签到').wait()
        # 向上滑动80%
        self.d.swipe_ext("up", 0.6)
        # 等待日常任务出现
        self.d(text='社区圈子发帖').wait()
        # 检查当前任务进度
        task1 = self.d(text='5/5 +3积分').exists
        task3 = self.d(text='8/8 +1积分').exists
        return task1,task3


    # 任务中心页面。选择指定任务
    def task_center(self):
        # 获取任务进度
        task1,task3 = self.get_task()
        while not task1:
            # 点击 社区发帖 去完成按钮
            self.d.xpath(
                '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/daily_clock_on_novice_tasks_list2"]/android.view.ViewGroup[1]/android.widget.TextView[1]').click_exists()
            self.post_content()
            task1, task3 = self.get_task()

        print('开始执行任务3')
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
            task1, task3 = self.get_task()


            # self.d(text='首页').wait()
            # # 点击我的
            # self.d.xpath(
            #     '//*[@resource-id="com.timanetworks.android.faw.vw.aftermarket.release:id/user_item"]/android.widget.ImageView[1]').click()
            #
            # self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/tv_menu", text="任务中心").click()
            #
            # self.d(text='每日签到').wait()
            # # 向上滑动80%
            # self.d.swipe_ext("up", 0.6)
            # # 等待日常任务出现
            # self.d(text='社区圈子发帖').wait()

        print('日常任务执行完成')


    # 编写帖子内容，并发布
    def post_content(self):
        # 添加主题
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/tv_theme").click()
        self.d(text='选择主题').wait()
        # 向上滑动80%
        self.d.swipe_ext("up", 0.6)
        # 选择双周打卡
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/circle_topic_item_name_txt",
          text="双周早起打卡挑战").click_exists()

        # 选中标题
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/new_bbs_title_edit").click()
        self.d.set_fastinput_ime(True)
        self.d.send_keys("祝大家虎年虎虎生威")
        # 选中内容
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/rich_editor_item_edit_text").click()
        self.d.send_keys("新年双周打开，新年快乐 万事如意 诸事顺利 心想事成天天开心 幸福美满 阖家欢乐 福星高照喜上眉梢 欢天喜地 财运亨通 吉祥如意工作顺利 龙马精神 寿比南山 步步高升")
        self.d.set_fastinput_ime(False)
        # 点击发布
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/top_action_bar_right_text").click()

    # 进行评论
    def comment(self):
        self.d(text='我也来说一句...').wait()
        # 选中评论输入框
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/write_comment_bar").click()
        self.d.set_fastinput_ime(True)
        self.d.send_keys("666666666666")
        self.d.set_fastinput_ime(False)
        # 发布评论
        self.d(resourceId="com.timanetworks.android.faw.vw.aftermarket.release:id/comment_publish_btn").click()

    def run(self):
        self.start()
        self.minitorwindow()
        self.mypage()
        self.task_center()

# 常用命令
# d(text="收益明细").exists    检索页面是否有收益明细 并返回布尔值
# d(text="收益明细").info       获取ui对象信息
# d(text="提现记录").click()    点击
# d(text="银行卡已到账").count     统计相同条件的数目
# d.swipe(0.107, 0.936, 0.176, 0.179)    向上滑动 参数为坐标
# d.double_click(0.847, 0.061)      对指定坐标 进行双击操作

if __name__ == '__main__':
    device_serNo = adbutils.adb.device_list()[0].serial
    print(device_serNo)
    d = u2.connect(device_serNo)
    a = autoScore(d)
    a.run()











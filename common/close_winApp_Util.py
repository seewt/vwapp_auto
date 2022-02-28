import os,psutil

def close_app(processName):
    # 获取进程id
    def get_pid(pname):
        for proc in psutil.process_iter():
            # print(“pid-%d,name:%s” % (proc.pid,proc.name()))
            if proc.name() == pname:
                return proc.pid
    # 关闭进程
    os.popen('taskkill /pid ' + str(get_pid(processName)))


if __name__ == '__main__':
    close_app('Nox.exe')
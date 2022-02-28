import os
import subprocess

# print(subprocess.run(['ipconfig']))

# print(subprocess.getoutput('ping www.baidu.com -t'))
# print(subprocess.getoutput('ipconfig'))
#
print(os.popen('ipconfig').readlines())
# res = subprocess.getoutput('ipconfig')
# print(res[1:1])
# print(type(res[1]))
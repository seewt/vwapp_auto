import os

# print(os.system('ping www.baidu.com -t'))
# print(os.system('ipconfig'))



print(os.popen('ping www.baidu.com -t').readlines())
print(os.popen('ipconfig').read())
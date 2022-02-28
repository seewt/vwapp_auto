import os
# 执行操作系统的命令，将结果输出到屏幕，只返回命令执行状态(0：成功，非 0 ： 失败)
# 注意返回的是执行命令的状态，通常是0 和非 0
print(os.system('ipconfig'))
print(os.popen('ipconfig'))

print('-------------------')

print(os.popen('ipconfig').read())

print('-------------------')
ipconfig=os.popen('ipconfig').readlines()
print(ipconfig)
for line in ipconfig:
    print(line.strip())
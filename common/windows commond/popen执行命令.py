import os


'''
读取的时候注意光标位置,进行字符串处理的时候 需要对换行符号进行处理
'''
# 返回对应命令的输出结果
res = os.popen('adb devices')
# 读取全部(字符串)
print(res.read())
# 每次读取一行
print(res.readline())
# 读取整个文件，并将整个文件按行解析成列表,
print(res.readlines())

print(os.popen('ipconfig').read())

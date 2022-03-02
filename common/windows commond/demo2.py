import os

#1111
res = os.popen('adb connect 127.0.0.1')._stream
res2 = res.buffer.read().decode(encoding='utf-8', errors ='ignore')
print(res2)

# print(os.system('adb connect 127.0.0.1'))
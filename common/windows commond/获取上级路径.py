import os

image = os.path.abspath(os.path.dirname(os.getcwd())) + "\\excute_image\\1.jpg"








cmd ="adb push "+os.path.abspath(os.path.dirname(os.getcwd()))+"\\excute_image\\pic.png "+ "/sdcard/Pictures"

print(cmd)


print(image)

os.popen("adb push" + os.path.abspath(os.path.dirname(os.getcwd())) + "\\excute_image\\pic.png " + "/sdcard/Pictures")

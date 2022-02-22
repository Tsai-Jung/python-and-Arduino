import serial   #导入串口通讯库
import pyautogui
import time
ser=serial.Serial("com4",9600,timeout=1)

#只有0-9可以用
while 1:
    text=ser.read(1000)
    #print(text)#一次读取多少行
    text=str(text)
    text = text.split("'")
    try:
        #print(text[1])
        text = text[1].split("\\")
        #print(text[0])
        if(text[0]=='BA0F4EDF'):
            print('确定键')
            pyautogui.press('space')
        elif(text[0]=='450753D6'):
            print('倒退')
            pyautogui.press('left')
        elif(text[0]=='4AC4DA9A'):
            print('快进')
            pyautogui.press('right')
    except:
        pass

import serial   #导入串口通讯库

ser=serial.Serial("com4",9600,timeout=1)

#只有0-9可以用
while 1:
    text=ser.read(100)
    #print(text)#一次读取多少行
    text=str(text)
    text = text.split("'")
    try:
        #print(text[1])
        text = text[1].split("\\")
        print(text[0])
    except:
        pass

import serial   #导入串口通讯库

ser=serial.Serial("com4",9600,timeout=1)

#只有0-9可以用
while 1:
    c = input('请输入指令:')
    c=b"%d"%int(c)
    print(c)
    ser.write(c)

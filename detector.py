# TODO 串口读取数据
# Auther HJC

import serial  # 导入串口包
import time  # 导入时间包

ser = serial.Serial("COM3", 115200, timeout=5)  # 开启com3口，波特率115200，超时5
ser.flushInput()  # 清空缓冲区


def detector():
    while True:
        count = ser.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            recv = ser.read(ser.in_waiting)  # 读出串口数据，数据采用gbk编码
            a = bytearray(recv)
            if a[1]==10:
                # print(a[1])
                # print(type(a[1]))
                b = str(hex(a[11]))[2:]
                c = str(hex(a[12]))[2:]
                if(len(c)==1):
                    c="0"+c
                print(b)
                print(c)

                d = b + c
                print(d)
                height = int(d, 16) * 2 / 100
                print(height, end=' ')
                print('cm')
                return height
            # b = recv[:-1]
            # print(int.from_bytes(recv, byteorder='big', signed=False))
            # print(time.time()," ---  recv --> ", recv)  # 打印一下子
        time.sleep(0.1)  # 延时0.1秒，免得CPU出问题


def detector1():
    while True:
        count = ser.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            recv = ser.read(ser.in_waiting)  # 读出串口数据，数据采用gbk编码
            a = bytearray(recv)
            if a[1]==11:
                b = str(hex(a[11]))  # 温度
                temperature = int(b, 16)
                print(temperature, end=' ')
                return temperature
            # b = recv[:-1]
            # print(int.from_bytes(recv, byteorder='big', signed=False))
            # print(time.time()," ---  recv --> ", recv)  # 打印一下子
        time.sleep(0.1)  # 延时0.1秒，免得CPU出问题





if __name__ == '__main__':
    m = detector()

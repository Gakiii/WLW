# TODO 串口读取数据
# Auther wjw

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
            if len(a) == 13:
                b = str(hex(a[11]))[2:]
                c = str(hex(a[12]))[2:]
                d = b + c
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
            if len(a) == 14:
                b = str(hex(a[11]))  # 温度
                temperature = int(b, 16)
                print(temperature, end=' ')
                return temperature
            # b = recv[:-1]
            # print(int.from_bytes(recv, byteorder='big', signed=False))
            # print(time.time()," ---  recv --> ", recv)  # 打印一下子
        time.sleep(0.1)  # 延时0.1秒，免得CPU出问题



# def temperatureDetecte():
#     while True:
#         count = ser.inWaiting()  # 获取串口缓冲区数据
#         if count != 0:
#             recv = ser.read(ser.in_waiting)  # 读出串口数据，数据采用gbk编码
#             a = bytearray(recv)
#             if len(a) == 14:
#                 b = str(hex(a[11]))  # 温度
#                 # c = str(hex(a[12]))[2:]
#                 temperature = int(b, 16)
#                 print(temperature, end=' ')
#                 print('‘C')
#
#                 #return temperature
#
#             # b = recv[:-1]
#             # print(int.from_bytes(recv, byteorder='big', signed=False))
#             # print(time.time()," ---  recv --> ", recv)  # 打印一下子
#         time.sleep(0.1)  # 延时0.1秒，免得CPU出问题


if __name__ == '__main__':
    m = detector()
    print(m[0][:-2])
    print(m[1][:-2])

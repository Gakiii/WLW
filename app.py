from concurrent.futures import thread

from flask import Flask, render_template
import  detector

app = Flask(__name__)  # 绑定app


# 函数一：关联页面
@app.route('/')  # 路由
def image():
    return render_template('image.html')

@app.route('/temperature')  # 路由
def image2():
    return render_template('temperature.html')

# 函数二：生成数据
from flask import jsonify  # 数据转为json，并以字典的形式传回前端
import datetime, random  # 导入时间和随机数模块


# @app.route('/setData/')  # 路由
# def setData():
#     while True:
#         print("hello world")
#         now = datetime.datetime.now().strftime('%H:%M:%S')
#         array = detector.detector()
#         height = 0
#         temperature = 0
#         a = array[0]
#         b = array[1]
#         if a[-2:-1] == 'm':
#             height = float(a[:-2])
#             temperature=float(b[:-2])
#         else:
#             height = float(b[:-2])
#
#             temperature = float(a[:-2])
#
#         data = {'time':now, 'h':height,'t':temperature}
#         #data = {'time': now, 'data': random.randint(1, 10)}
#         return jsonify(data)  # 将数据以字典的形式传回

@app.route('/setData/')
def setData():
    while True:
        print("hello world")
        now = datetime.datetime.now().strftime('%H:%M:%S')
        height = detector.detector()
        data = {'time':now, 'data':height}
        #data = {'time': now, 'data': random.randint(1, 10)}
        return jsonify(data)  # 将数据以字典的形式传回

@app.route('/setData1/')
def setData1():
    while True:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        temperature = detector.detector1()
        data = {'time':now, 'data':temperature}
        #data = {'time': now, 'data': random.randint(1, 10)}
        return jsonify(data)  # 将数据以字典的形式传回

# @app.route('/setData2/')
# def setDataTemperature():
#     while True:
#         print("hello world")
#         now = datetime.datetime.now().strftime('%H:%M:%S')
#         temperature = detector.temperatureDetecte()
#         data = {'time':now, 'data':temperature}
#         #data = {'time': now, 'data': random.randint(1, 10)}
#         return jsonify(data)  # 将数据以字典的形式传回

if __name__ == '__main__':
    app.run()
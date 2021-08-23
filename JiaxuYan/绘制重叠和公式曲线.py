#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@Author  :   Celeste Young
@File    :   绘制重叠和公式曲线.py    
@Time    :   2021/8/15 12:41  
@E-mail  :   iamwxyoung@qq.com
@Tips    :   
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getData():
    return pd.read_excel(r'E:\桌面文件备份\twist\新建文件夹\300_0.01.xls')


def getLm(a_, theta_, m_n=1):
    # a_ = 142 || 246
    canshu = 18  # 该参数是为了把曲线归一化
    theta_ = np.deg2rad(theta_)
    if m_n == 1:
        return a_ / (2 * (np.sin(theta_ / 2.0))) / canshu
    else:
        return m_n * a_ / (2 * (np.sin(theta_ / 2.0))) / canshu


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    title = ['angle', 'over_lap_ratio']
    dataSet = np.array(getData()[title])
    xRange = np.linspace(1, 30, 290)
    y142 = getLm(142, xRange)
    y246 = getLm(246, xRange)
    y284 = getLm(142, xRange, 2)
    y492 = getLm(246, xRange, 2)
    y568 = getLm(142, xRange, 4)
    y710 = getLm(142, xRange, 5)
    plt.plot(xRange[2:], y142[2:], label='142.0')
    plt.plot(xRange[10:], y246[10:], label='246.0')
    plt.plot(xRange[20:], y284[20:], label='284.0')
    plt.plot(xRange[100:], y492[100:], label='492.0')
    plt.plot(xRange[130:], y568[130:], label='568.0')
    plt.plot(xRange[70:], y710[70:], label='710.0')
    plt.plot(dataSet[100:, 0], 100/dataSet[100:, 1], color='black', linewidth='0.1', label='ratio')  # 筛选出较高的序列
    plt.title('ratio-distance')
    plt.legend(loc='upper right')
    plt.show()

    # print(dataSet[:10, 0], 12/dataSet[:10, 1])
#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@Author  :   Celeste Young
@File    :   绘制TBG equation.py    
@Time    :   2021/7/31 10:09  
@E-mail  :   iamwxyoung@qq.com
@Tips    :   TBG equation单调性是怎样的？
'''

import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
import math


def getLm(a_, theta_):
    theta_ = np.deg2rad(theta_)
    return a_ /(2 * (np.sin(theta_ / 2.0)))


if __name__ == '__main__':

    a = 246
    x1 = np.linspace(2, 60, 600)
    y1 = getLm(a, x1)

    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(x1, y1, color='blue')
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.plot(x1,y1)
    # ax.fill_between(x, f(x), color='green', alpha=0.5)
    # plt.axhline(y=0, xmin=0, xmax=1, linestyle='--', color='grey')
    # plt.axvline(x=0.5, ymin=0, ymax=1, linestyle='--', color='grey')
    # plt.axvline(x=0,ymin=0,ymax=1,linestyle='--',color='grey')
    # plt.axvline(x=1,ymin=0,ymax=1,linestyle='--',color='grey')
    plt.show()

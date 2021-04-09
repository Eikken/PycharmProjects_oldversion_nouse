#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@Author  :   Celeste Young
@File    :   twistGrapheneTest.py    
@Time    :   2021/3/20 11:46  
@E-mail  :   iamwxyoung@qq.com
@Tips    :   先生成石墨烯结构，然后zip打包[xList,yList]，进行M(θ)角度的旋转并进行plt.show()
        min.(axis = )none：整个矩阵; 0：每列; 1：每行

'''

import math
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import distance
import xlwt
import time
import pandas as pd


class Circle:
    x = 0.0
    y = 0.0
    r = 1.0

    def __init__(self, x, y, R):
        self.x = float(x)
        self.y = float(y)
        self.r = float(R)

    def calArea(self):
        return np.pi * self.r ** 2


# 求两圆相交的面积
def calShadow(circle1, circle2):
    d = ((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2) ** 0.5
    if d == 0:
        return circle1.calArea()
    if d > 14:
        print('[', circle1.x, ',', circle1.y, '] 和 [', circle2.x, ',', circle2.y, ']不重叠')
        return 0.0
    else:
        ang1 = np.arccos((circle1.r ** 2 + d ** 2 - circle2.r ** 2) / 2.0 / circle1.r / d)
        ang2 = np.arccos((-circle1.r ** 2 + d ** 2 + circle2.r ** 2) / 2.0 / circle2.r / d)
        area = ang1 * circle1.r ** 2 + ang2 * circle2.r ** 2 - d * circle1.r * np.sin(ang1)
        return area


def calTotal(initMox, bs=1):
    circle = Circle(0, 0, 0.07*bs)
    pointsNum = len(initMox)
    total_area = pointsNum * circle.calArea()
    return total_area


# 求list中圆相交的总面积
def sumArea(set1, set2, bs=1):
    emptyList = []
    for s in set1:
        minDistance = distance.cdist([s], set2, 'euclidean').min(axis=1)
        indexTuple = np.where(distance.cdist(set2, [s], 'euclidean') == minDistance)
        # set2[indexTuple[0]][0]是准确的数据
        result = calShadow(Circle(s[0], s[1], 0.07 * bs),
                           Circle(set2[indexTuple[0]][0][0], set2[indexTuple[0]][0][1], 0.07 * bs))
        emptyList.append(result)
    return sum(emptyList)


def genGraphene(Super=10, bs=1):  # 返回新的坐标的大胞
    # 原胞中C的坐标
    a = (2.460, 0, 0)
    b = (2.460 / 2, 2.460 / 2 * math.sqrt(3), 0)
    c = (0, 0, 20)
    # 扩胞矩阵
    super_x = Super
    super_y = Super
    super_z = 1

    extendCellMatrix = np.array([[super_x, 0, 0],
                                 [0, super_y, 0],
                                 [0, 0, super_z]])
    lattice = np.array([a, b, c])
    # 矩阵右乘扩胞矩阵3X3 * 3X3，生成新的大胞
    extendLattice = np.dot(lattice, extendCellMatrix)
    # C1 = [0, 0, 0.5]
    # C2 = [1 / float(3), 1 / float(3), 0.5]
    Frac1 = 0
    Frac2 = 1 / float(3)
    allAtoms = []
    for i in range(super_x):
        for j in range(super_y):
            newC1 = [(Frac1 + i) / super_x, (Frac1 + j) / super_y, 0.5]
            newC2 = [(Frac2 + i) / super_x, (Frac2 + j) / super_y, 0.5]
            allAtoms.append(newC1)
            allAtoms.append(newC2)
    newAllAtoms = np.dot(np.array(allAtoms), extendLattice)
    x_List = np.array(newAllAtoms).T[0] * bs
    y_List = np.array(newAllAtoms).T[1] * bs
    z_List = np.array(newAllAtoms).T[2] * bs
    x_Mean = np.mean(x_List)
    y_Mean = np.mean(y_List)
    x_List = x_List - np.mean(x_List)
    y_List = y_List - np.mean(y_List)
    return x_List, y_List, z_List, x_Mean, y_Mean


def matrixTransformation(x_, y_, theta):
    Matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    xT, yT = [], []
    for k, v in zip(x_, y_):
        twistMatrix = np.dot([k, v], Matrix)
        # 矩阵 1X2 * 2X2 = 1X2
        xT.append(twistMatrix[0])
        yT.append(twistMatrix[1])
    return np.array(xT), np.array(yT)


# 画圆函数
def f(x, R):
    return (R ** 2 - x ** 2) ** 0.5


# 计算(x,y)和原点(0,0)的距离
def normXY(xx, yy):
    return (xx ** 2 + yy ** 2) ** 0.5


def doublePointsDistance(ix, iy, tx, ty):
    return ((tx - ix) ** 2 + (ty - iy) ** 2) ** 0.5


def overFlowDrop(xL, yL, R):
    xDrop = np.delete(xL, np.where(xList.__abs__() > R))  #
    yDrop = np.delete(yL, np.where(xList.__abs__() > R))
    return xDrop, yDrop


# initXY是未旋转的初始坐标集合，twistXY是旋转后的坐标集合，两者计算overlap


def drawFig(x1, y1, x2, y2, angleTheta, r):
    xIndex = np.linspace(-r, r, int(r))
    plt.figure(figsize=(9, 8), edgecolor='black')
    plt.subplot(111)
    plt.scatter(x1, y1, 1, marker='.', color='green')
    plt.scatter(x2, y2, 1, marker='.', color='blue')
    plt.plot(xIndex, f(xIndex, r), lw=1, color='red')
    plt.plot(xIndex, -f(xIndex, r), lw=1, color='red')
    # plt.savefig('png/area_twist_%.3f°.png' % angleTheta, dpi=1000)
    print('showed')  # , saved area_twist_%.3f°.png' % angleTheta)
    plt.show()


def drawOverLap(set1, set2, angleTheta):
    plt.scatter(set1[:, 0], set1[:, 1], 15, marker='*', color='green')
    plt.scatter(set2[:, 0], set2[:, 1], 5, marker='.', color='red')
    plt.scatter(0, 0, 10, marker='*', color='black')
    # plt.savefig('png/over_lap_%.2f°.png' % angleTheta, dpi=1000)
    print('showed')  # saved over_lap_%.2f°.png' % angleTheta)
    plt.show()


def calEuclidean(s_1, s_2):
    # s1 为列标，s2为行标，求s2内的点到s1中每个点最近的，就得取行最小值。
    dis1 = distance.cdist(s_1, s_2, 'euclidean').min(axis=1)
    dis2 = distance.cdist(s_1, s_2, 'euclidean').min(axis=0)
    index_S1 = np.where(dis1 < 14)
    index_S2 = np.where(dis2 < 14)
    # df = pd.DataFrame(distance.cdist(s1, s2, 'euclidean')) # 数据转Excel
    # df.to_excel('data/%.3f°distance.xlsx'%angle, index=True, header=True)
    return index_S1, index_S2


if __name__ == '__main__':
    t1 = time.time()
    bs = 100
    Super = 50
    xList, yList, zList, xMean, yMean = genGraphene(Super=Super, bs=bs)
    # 绘制圆
    x_Drop, y_Drop = overFlowDrop(xList, yList, yMean)  # 注意你删除的原子的方式
    r = yMean
    mox = np.delete(x_Drop, np.where(normXY(x_Drop, y_Drop) > r))
    moy = np.delete(y_Drop, np.where(normXY(x_Drop, y_Drop) > r))

    totalArea = calTotal(mox, bs=bs)

    # 下面部分可以定义一个写Excel的函数
    book = xlwt.Workbook()  # 创建Excel
    sheet = book.add_sheet('sheet1')
    title = ['angle', 'over_lap_area', 'over_lap_number', 'over_lap_ratio']  # over_lap_number是多少对原子重叠
    row = 0  # 行
    col = 0  # 列
    for t in title:
        sheet.write(row, col, t)
        col += 1
    for i in range(0, 3600):
        row += 1  # 行加一
        col = 0  # 从第0列开始写
        content = []  # 临时内容列表写入excel文件
        angle = i * 0.1
        thetaAngle = np.pi * angle / 180.0
        xTwist, yTwist = matrixTransformation(mox, moy, thetaAngle)
        s1 = np.stack((mox, moy), axis=-1)
        s2 = np.stack((xTwist, yTwist), axis=-1)
        indexS1, indexS2 = calEuclidean(s1, s2)
        overLapArea = sumArea(s1[indexS1], s2[indexS2], bs=bs)
        overLapRatio = overLapArea/totalArea
        content.append(angle)
        content.append(overLapArea)
        content.append(len(indexS1[0]))
        content.append(overLapRatio*100)
        for j in content:
            sheet.write(row, col, j)
            col += 1
    book.save('data/%dExpansion.xls' % Super)

    # while True:
    #     angle = float(input('请输入逆时针旋转角度：'))
    #     if angle == 0.0:
    #         break
    #     thetaAngle = np.pi * angle / 180.0
    #     xTwist, yTwist = matrixTransformation(mox, moy, thetaAngle)
    #     s1 = np.stack((mox, moy), axis=-1)
    #     s2 = np.stack((xTwist, yTwist), axis=-1)
    #     indexS1, indexS2 = calEuclidean(s1, s2)
    #
    #     # sortS1 = sorted(s1[indexS1], key=lambda s1_values: s1_values[0] + s1_values[1])
    #     # sortS2 = sorted(s2[indexS2], key=lambda s2_values: s2_values[0] + s2_values[1])
    #
    #     overLapArea = sumArea(s1[indexS1], s2[indexS2], bs=bs)
    #     print('共%d对重叠' % (len(indexS1[0])), '重叠面积为%.6f' % overLapArea)
    #     drawOverLap(s1[indexS1], s2[indexS2], angle)
    #     # 计算加和、按坐标的x,y分别排序都不行。
    #     # 下面一行为画circle twist
    #     # drawFig(mox, moy, xTwist, yTwist, angle, yMean)
    #     # drawFig(xList, yList)
    t2 = time.time()
    print('Finish, use time', t2 - t1, 's')
# # 设置x y轴的长度为 1:1
# ax = plt.gca()
# ax.set_aspect(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Email: aimer.neige@aimerneige.com

"""
战斗机机翼外形根据工艺要求由一组数据 (x,y) 给出，
用程控铣床加工对每一刀只能沿 x 方向和 y 方向切割很小的一步，
因此需要从已知数据得到满足加工所要求的步长很小的每一步坐标。
下表给出的 x, y 数据位于机翼断面的下轮廓上，
假设需要得到 x 坐标每改变 0.1 时的 y 坐标，
试完成加工所需要数据，
并画出曲线。
x 0 3 5 7 9 11 12 13 14 15
Y 0 1.2 1.7 2.0 2.1 2.0 1.8 1.2 1.0 1.6
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi


# 插值函数
def spline_interpolation(X, Y):
    ipo = spi.splrep(X, Y, k=5)
    return ipo


# 绘制曲线
def draw_curve(X, Y, x, iy):
    plt.plot(X, Y, 'o', label='original data')
    plt.plot(x, iy, '-', color='red', label='spline interpolation')
    plt.legend()
    plt.show()


def main():
    X = np.array([0, 3, 5, 7, 9, 11, 12, 13, 14, 15])
    Y = np.array([0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6])
    x = np.arange(0, 15, 0.15)
    ipo = spline_interpolation(X, Y)
    iy = spi.splev(x, ipo)
    draw_curve(X, Y, x, iy)


if __name__ == '__main__':
    main()

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

# 拉格朗日插值
def lagrange_interpolation(x, y):
    """

    :param x: x 坐标
    :param y: y 坐标
    :return: x_new, y_new 插值点
    """
    x_new = np.arange(x[0], x[-1], 0.1)
    y_new = np.zeros(x_new.shape)
    for i in range(len(x_new)):
        for j in range(len(x)):
            y_new[i] += y[j] * lagrange_interpolation_single(x, y, x_new[i], j)
    return x_new, y_new


# 拉格朗日插值单个点
def lagrange_interpolation_single(x, y, x_new, j):
    result = 1
    for i in range(len(x)):
        if i != j:
            result *= (x_new - x[i]) / (x[j] - x[i])
    return result


# 图像绘制
def draw_curve(x, y, x_new, y_new):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o', label='original data')
    plt.plot(x_new, y_new, '-', label='lagrange interpolation')
    plt.title('lagrange interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def main():
    x = np.array([0, 3, 5, 7, 9, 11, 12, 13, 14, 15])
    y = np.array([0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6])
    x_new, y_new = lagrange_interpolation(x, y)
    draw_curve(x, y, x_new, y_new)


if __name__ == '__main__':
    main()

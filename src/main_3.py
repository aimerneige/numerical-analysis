#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Email: aimer.neige@aimerneige.com

"""
某乡镇企业 2010 - 2016 年的大致生产利润如下表
试采用正确的方法预测 2017 和 2018 年的利润
年份 2010 2011 2012 2013 2014 2015 2016
利润(万元) 70 122 144 152 174 196 202
"""

import numpy as np
import matplotlib.pyplot as plt


def least_squares(x, y):
    """
    最小二乘法
    :param x: 自变量
    :param y: 因变量
    :return: 拟合系数
    """
    x = np.array(x)
    y = np.array(y)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_ = x - x_mean
    y_ = y - y_mean
    x_y = np.sum(x_ * y_)
    x_x = np.sum(x_ ** 2)
    a = x_y / x_x
    b = y_mean - a * x_mean
    return a, b


def draw_curve(x, y, a, b):
    """
    绘制拟合曲线
    :param x: 自变量
    :param y: 因变量
    :param a: 拟合系数
    :param b: 拟合系数
    :return:
    """
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, a * x + b, label='fitted line')
    plt.xlabel('Year')
    plt.ylabel('Profit(10,000)')
    plt.legend()
    plt.show()


def main():
    x = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
    y = [70, 122, 144, 152, 174, 196, 202]
    a, b = least_squares(x, y)
    print('拟合系数：')
    print('a =', a)
    print('b =', b)
    print('拟合函数：')
    print('y =', a, 'x +', b)
    print('预测结果：')
    print('2017 年的利润：', a * 2017 + b)
    print('2018 年的利润：', a * 2018 + b)
    draw_curve(x, y, a, b)


if __name__ == '__main__':
    main()


# 拟合系数：
# a = 20.5
# b = -41115.07142857143
# 拟合函数：
# y = 20.5 x + -41115.07142857143
# 预测结果：
# 2017 年的利润： 233.42857142857247
# 2018 年的利润： 253.92857142857247

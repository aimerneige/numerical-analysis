#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Email: aimer.neige@aimerneige.com

"""
分别用二分法和牛顿法求方程
f(x) = x^3 - 2x - 5 = 0
在区间 [2,3] 内的根，
观察两种方法的迭代次数，
并说明原因。
"""

import time


def math_function(x):
    return x ** 3 - 2 * x - 5


def dichotomy(a, b, epsilon):
    """
    二分法
    :param a: 左边界
    :param b: 右边界
    :param epsilon: 精度
    :return: 根，迭代次数
    """
    n = 0
    while abs(a - b) > epsilon:
        n += 1
        x = (a + b) / 2
        if math_function(x) > 0:
            b = x
        else:
            a = x
    return x, n


def newton(x, epsilon):
    """
    牛顿法
    :param x: 初始值
    :param epsilon: 精度
    :return: 根，迭代次数
    """
    n = 0
    while abs(math_function(x)) > epsilon:
        n += 1
        x = x - math_function(x) / (3 * x ** 2 - 2)
    return x, n


def main():
    a = 2
    b = 3
    epsilon = 1e-5
    start = time.time()
    x, n = dichotomy(a, b, epsilon)
    end = time.time()
    dichotomy_time = end - start
    print('二分法根：', x)
    print('二分法迭代次数：', n)
    print('二分法迭代时间：', dichotomy_time)
    start = time.time()
    x, n = newton(a, epsilon)
    end = time.time()
    newton_time = end - start
    print('牛顿法根：', x)
    print('牛顿法迭代次数：', n)
    print('牛顿法迭代时间：', newton_time)


if __name__ == '__main__':
    main()


# 分法根： 2.0945510864257812
# 二分法迭代次数： 17
# 二分法迭代时间： 2.384185791015625e-05
# 牛顿法根： 2.094551481698199
# 牛顿法迭代次数： 3
# 牛顿法迭代时间： 9.5367431640625e-06

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Email: aimer.neige@aimerneige.com

"""
用原始高斯消去法、列主元消去法分别求解方程组，并比较结果的精度
0.9428 x1 + 0.3475 x2 - 0.8468 x3 = 0.4127
0.3475 x1 + 1.8423 x2 + 0.4759 x3 = 1.7321
-0.8468 x1 + 0.4759 x2 + 1.2147 x3 = -0.8621
"""

import numpy as np
import time


def gauss_elimination(A, b):
    """
    原始高斯消去法
    :param A: 系数矩阵
    :param b: 右端项
    :return: 解
    """
    n = len(A)
    for k in range(n - 1):
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[k][k]):
                A[[k, i]] = A[[i, k]]
                b[[k, i]] = b[[i, k]]
            else:
                continue
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            b[i] = b[i] - m * b[k]
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + A[i][j] * x[j]
        x[i] = (b[i] - s) / A[i][i]
    return x


def gauss_elimination_pivot(A, b):
    """
    列主元消去法
    :param A: 系数矩阵
    :param b: 右端项
    :return: 解
    """
    n = len(A)
    for k in range(n - 1):
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[k][k]):
                A[[k, i]] = A[[i, k]]
                b[[k, i]] = b[[i, k]]
            else:
                continue
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            b[i] = b[i] - m * b[k]
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + A[i][j] * x[j]
        x[i] = (b[i] - s) / A[i][i]
    return x


if __name__ == '__main__':
    A = np.array([[0.9428, 0.3475, -0.8468], [0.3475, 1.8423, 0.4759], [-0.8468, 0.4759, 1.2147]])
    b = np.array([0.4127, 1.7321, -0.8621])
    start = time.time()
    x = gauss_elimination(A, b)
    end = time.time()
    gauss_elimination_time = end - start
    print('原始高斯消去法解为：', x)
    print('原始高斯消去法运行时间为：', gauss_elimination_time)
    start = time.time()
    x = gauss_elimination_pivot(A, b)
    end = time.time()
    gauss_elimination_pivot_time = end - start
    print('列主元消去法解为：', x)
    print('列主元消去法运行时间为：', gauss_elimination_pivot_time)

# 原始高斯消去法解为： [-14.05184157   7.01437233 -13.2537575 ]
# 原始高斯消去法运行时间为： 3.838539123535156e-05
# 列主元消去法解为： [-14.05184157   7.01437233 -13.2537575 ]
# 列主元消去法运行时间为： 2.09808349609375e-05

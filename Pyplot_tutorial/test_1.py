# coding:utf-8

from matplotlib import pyplot as plt
import numpy as np


plt.plot([1, 2, 3, 4])
# PS：只有一个列表则默认为y轴，x轴自动生成跟y轴一样长度(起点可能不一样)
plt.ylabel('test numbers')  # 定义标题
plt.show()                  # 显示图像


plt.plot([1, 2, 3, 4,], [1, 4, 9, 16], 'ro')    # 完整参数分别为：x轴座标点，y轴座标点，画图样式
plt.axis([0, 6, -10, 10])                       # 定义坐标轴上下限
plt.show()


# 以0.2s的时间间隔从0到5均匀采样创建一个矩阵
t = np.arange(0., 5., 0.2)


# 红色虚线、蓝色方块和绿色三角形
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()



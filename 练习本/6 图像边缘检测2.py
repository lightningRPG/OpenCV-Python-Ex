# coding:utf-8
# """Canny算子的边缘检测"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


lena = "../pictures/lena.png"
gray_img = cv.imread(lena, 0)
# """
#     Canny算子的运算过程
#     1. 降噪（Canny算子对噪声敏感，得降噪——一般用的5x5高斯滤波
#     2. 寻找图像梯度的强度（找到每个像素点的梯度方向和强度
#     3. 抑制非最大值（检查像素是否在梯度方向的邻域中是局部最大值，不是则置零
#     4. 滞后阈值（设定最大值与最小值筛选掉不明确的边缘
# """
canny_img = cv.Canny(gray_img, 100, 200)    # 用Canny算子获取图像边缘
# 100 和 200 分别是筛选边缘用的最小值和最大值

# 显示图像
plt.subplot(121), plt.imshow(gray_img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(canny_img, cmap='gray')
plt.title('Canny Image'), plt.xticks([]), plt.yticks([])

plt.show()

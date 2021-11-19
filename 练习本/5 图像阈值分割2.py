# coding: utf-8
# """自适应阈值图像分割"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


lena = "../pictures/lena.png"
color_img = cv.imread(lena, cv.IMREAD_COLOR)
gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)
# gray_img = cv.medianBlur(gray_img, 5)     # 中值滤波

maxval = 255    # 处理图像用的像素点最大灰度值
thresh = 127    # 用于图像分割的固定阈值(与返回值ret是相等的)
ret, th1_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_BINARY)     # 简单阈值（作对比用
# 自适应阈值均值模式
th2_img = cv.adaptiveThreshold(     # 阈值 T 由(x,y)的blockSize×blockSize邻域的平均值减去C得到
    gray_img, maxval, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=11, C=3)
# 自适应阈值高斯模式
th3_img = cv.adaptiveThreshold(     # 阈值 T 由(x,y)的blockSize×blockSize邻域减去C的加权和得到。
    gray_img, maxval, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize=21, C=3)
# blockSize 是邻域大小（通常为奇数
# C 是一个常数，用于被邻域的平均值或加权平均值减去


# 标题列表
titles = ['Original Image', 'Global Thresholding (v = 127)', 
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# 图像列表
images = [gray_img, th1_img, th2_img, th3_img]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

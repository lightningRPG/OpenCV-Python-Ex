# coding:utf-8
# """最大类间方差法 阈值图像分割"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


lena = "../pictures/lena.png"
color_img = cv.imread(lena, cv.IMREAD_COLOR)
gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)
# gray_img = cv.medianBlur(gray_img, 5)     # 中值滤波

maxval = 255    # 处理图像用的像素点最大灰度值
thresh = 127    # 用于图像分割的固定阈值(与返回值ret是相等的)
# 全局阈值
ret1, th1_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_BINARY)
# 最大类间方差法的阈值
ret2, th2_img = cv.threshold(gray_img, 0, maxval, cv.THRESH_BINARY+cv.THRESH_OTSU)
# 高斯滤波后的最大类间方差法的阈值
blur = cv.GaussianBlur(gray_img, (5, 5), 0)
ret3, th3_img = cv.threshold(blur, 0, maxval, cv.THRESH_BINARY+cv.THRESH_OTSU)

print("分割的阈值分别为%d, %d, %d" % (ret1, ret2, ret3))
# 显示所有图像
images = [gray_img, 0, th1_img, gray_img, 0, th2_img, blur, 0, th3_img]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    # 绘制灰度直方图
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    # 绘制阈值分割之后的图
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()

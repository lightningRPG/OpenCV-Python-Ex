# coding: utf-8
# """简单阈值图像分割"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


lena = "../pictures/lena.png"
color_img = cv.imread(lena, cv.IMREAD_COLOR)
gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)
# gray_img = cv.medianBlur(gray_img, 5)     # 中值滤波

maxval = 255    # 处理图像用的像素点最大灰度值
thresh = 127    # 用于图像分割的固定阈值(与返回值ret是相等的)
# 把灰度 高于thresh 的像素点赋值为maxval，其他像素点赋值为0
ret, thresh1_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_BINARY)
# 把灰度 高于thresh 的像素点赋值为0，其他像素点赋值为maxval
ret, thresh2_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_BINARY_INV)
# 把灰度 高于thresh 的像素点赋值为thresh，其他像素点保留（就是限制整幅图的灰度上限maxval也是没用的
ret, thresh3_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_TRUNC)
# 把灰度 高于thresh 的像素点保留，其他像素点赋值为0（那maxval不就没用了嘛
ret, thresh4_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_TOZERO)
# 把灰度 高于thresh 的像素点赋值为0，其他像素点保留
ret, thresh5_img = cv.threshold(gray_img, thresh, maxval, cv.THRESH_TOZERO_INV)
# ret 是分割使用的阈值

# 标题列表
titles = ["Original", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
# 图像列表
images = [gray_img, thresh1_img, thresh2_img, thresh3_img, thresh4_img, thresh5_img]

for i in range(6):
    plt.subplot(2, 3, i+1) 
    # """
    #     subplot三个参数分别表示：
    #         白板可容纳的图像行数，列数，当前图像所占位置
    # """
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)     # 显示图像
    # """
    #     imshow的参数：
    #         输入可以是实际的 RGB(A) 数据，也可以是 2D 标量数据，这些数据将被渲染为伪彩色图像。
    #         为了显示灰度图像，使用参数 cmap='gray', vmin=0, vmax=255 设置颜色映射。
    # """
    plt.title(titles[i])                                # 设置每幅图的标题
    # plt.xticks([500]), plt.yticks([100, 200])           # 标记图片边长的数值
    plt.xticks([]), plt.yticks([])                      

plt.show()

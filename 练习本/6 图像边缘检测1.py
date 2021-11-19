# coding:utf-8
# """拉普拉斯和Sobel算子的边缘检测"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


lena = "../pictures/lena.png"
color_img = cv.imread(lena, cv.IMREAD_COLOR)
gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)

# 图像边缘检测
laplacian_img = cv.Laplacian(gray_img, cv.CV_64F, ksize=9)      # 拉普拉斯算子
# """
#     Sobel算子是一个高斯平滑加微分的联合算子，
#     所以它对噪声的抵抗力更强。你可以指定导数的方向，
#     垂直或水平（分别通过参数yorder和xorder）。
#     你还可以通过参数ksize指定内核的大小。如果ksize = -1，
#     则使用3x3 Scharr滤波器比3x3 Sobel滤波器的结果更好。
# """
sobelx_img = cv.Sobel(gray_img, cv.CV_64F, 1, 0, ksize=9)       # Sobel算子(从看起来有光从左边照射)
sobely_img = cv.Sobel(gray_img, cv.CV_64F, 0, 1, ksize=9)       # (看起来有光从右边照射，ksize越大轮廓月明显)

# 显示图像
plt.subplot(2, 2, 1), plt.imshow(gray_img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(laplacian_img, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(sobelx_img, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(sobely_img, cmap='gray')
plt.title('Sobel Y')

plt.show()

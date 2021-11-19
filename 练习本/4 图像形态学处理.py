# coding:utf-8
# """图像的形态学处理"""

import numpy as np
import cv2 as cv

lena = "../pictures/lena.png"
color_img = cv.imread(lena, cv.IMREAD_COLOR)
gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)
# KERNEL = np.ones((5, 5), np.uint8)      # 用numpy创建一个卷积核(就是一个矩阵)
# 除了用numpy获取卷积核之外，openCV也提供了获取结构元素(卷积核)的方法
KERNEL = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))    # 获取5x5的矩形卷积核
KERNEL2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))    # 获取5x5的椭圆形卷积核
KERNEL3 = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))    # 获取5x5的十字形卷积核


def main():
    if (test_erosion()): print("图像腐蚀")

    if (test_dilation()): print("图像膨胀")

    if (test_opening()): print("图像开运算")

    if (test_closing()): print("图像闭运算")

    else: print("没有测试被启动")

    print("<<测试结束>>")

    return


# 腐蚀
def test_erosion():
    erosion_img = cv.erode(gray_img, KERNEL, iterations=1)  # 最后一个参数为腐蚀的次数
    cv.imshow("Gray", gray_img)
    cv.imshow("Erosion", erosion_img)
    cv.waitKey()

    return True


# 膨胀
def test_dilation():
    dilation_img = cv.dilate(gray_img, KERNEL, iterations=1)
    cv.imshow("Gray", gray_img)
    cv.imshow("Dilation", dilation_img)
    cv.waitKey()

    return True


# 开运算
def test_opening():
    opening_img = cv.morphologyEx(gray_img, cv.MORPH_OPEN, KERNEL)
    cv.imshow("Gray", gray_img)
    cv.imshow("Opening", opening_img)
    cv.waitKey()
    
    return True


# 闭运算
def test_closing():
    closing_img = cv.morphologyEx(gray_img, cv.MORPH_CLOSE, KERNEL)
    cv.imshow("Gray", gray_img)
    cv.imshow("Closing", closing_img)
    cv.waitKey()

    return True


if __name__ == '__main__':
    main()

# coding:utf-8
# """图像边缘提取及描绘"""

import numpy as np
import cv2 as cv

lena = '../pictures/lena.png'
color_img = cv.imread(lena)
# 使用cvtColor方法转换颜色空间(如：把RGB转成BGR)
gray_img = cv.cvtColor(color_img, cv.COLOR_BGR2GRAY)
# 阈值分割转化为二值图
ret, thresh_img = cv.threshold(gray_img, 127, 255, 0)
# 提取边缘
# """
#     第一个参数：
#         需要被提取的图像
#     第二个参数：(暂时无需深入，就用这个参数就好了)
#         检索所有的轮廓线，并重建一个完整的嵌套轮廓线层次。
#     第三个参数：
#         边缘点的展示方式（具体查看文档
#         SIMPLE  只显示必要的交点的点其他点省略
#         NONE    显示全部的点
# """
contours, hierarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(hierarchy)
# 描绘边缘
# """
#     第一个参数：
#         被描绘的图像
#     第二个参数：
#         需要描绘的点列表
#     第三个参数：
#         指示要绘制的轮廓的参数。如果为负，则绘制所有轮廓。
#     第四个参数：
#         描绘的线的颜色
#     第五个参数：
#         轮廓线的厚度
# """
contours_img = cv.drawContours(color_img.copy(), contours, -1, (0, 255, 0), 3)

# 显示图像
cv.imshow("contours_img", contours_img)
cv.imshow("color_img", color_img)
cv.waitKey()
cv.destroyAllWindows()


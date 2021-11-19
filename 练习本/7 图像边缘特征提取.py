# coding:utf-8
# """图像边缘特征提取"""

import numpy as np
import cv2 as cv

lena = '../pictures/lena.png'   # 这里并不建议使用lena的图，后期有空就把它换了吧，具体查看每个方法的作用，或者查看opencv的文档
lightning = '../pictures/ugly_lightning.png'
# gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)
gray_img = cv.imread(lena, 2)  # 跟上面注释的同等效果

# 先把边缘线搞出来
ret, thresh_img = cv.threshold(gray_img, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(thresh_img, 1, 2)     # 跟上面注释的同等效果，数字0则选择默认

# 计算多条轮廓的质心


def draw_moments_img(src, contours, r, start=0, end=len(contours), color=255):
    moment_img = src.copy()
    # 遍历每条边缘获取其图像矩，然后通过图像矩来计算其质心坐标
    for cnt_index in range(start, end):
        moments = cv.moments(contours[cnt_index])   # 获取单条边缘的图像矩
        if (moments['m00'] == 0):
            continue          # 不这样做是可能会报错的 :)
        cx = int(moments['m10']/moments['m00'])     # 通过固定公式计算质心 x 坐标
        cy = int(moments['m01']/moments['m00'])     # 通过固定公式计算质心 y 坐标
        # print(cx, cy)   # 打印来康康
        # 在图像中描出质心所在点
        for i in range(-r, r):
            x, y = cx + i, cy + i
            if (x < 512 and x > 0):
                moment_img[cx+i][cy] = color
            if (y < 512 and y > 0):
                moment_img[cx][cy+i] = color
    cv.imshow("moment img", moment_img)             # 显示图像


draw_moments_img(gray_img, contours, 5, start=0, end=100)

# ----------------------------------------------------------------------------------

# 以下测试使用这个图会好一点
gray_img2 = cv.imread(lightning, 2)
ret, thread = cv.threshold(gray_img2, 127, 255, 0)
contours2, hierarchy2 = cv.findContours(thread, 1, 2)
cv.imshow("gray_img2", gray_img2)

# 计算单条边缘的 面积
area = cv.contourArea(contours2[0])
print("area = ", area)

# 计算单条边缘的 周长
perimeter = cv.arcLength(contours2[0], True)
print("perimeter = ", perimeter)

# 计算单条边缘的 近似边缘（计算凸边缘的 凹面
epsilon = 0.1 * cv.arcLength(contours2[0], True)         # 计算边缘到近似边缘的最大距离
approx = cv.approxPolyDP(contours2[0], epsilon, True)    # 以指定的精度逼近多边形边缘。
# 以上的 bool 值参数都是指定近似边缘是否闭合

# 计算凹边缘的凸面
hull = cv.convexHull(contours2[0])
hull_img = gray_img2.copy()
cv.drawContours(hull_img, hull, -1, (0, 255, 0), 2)
cv.imshow("hull_img", hull_img)

# 判断一条边缘是否是凸的(没什么大不了的)
k = cv.isContourConvex(contours2[0])

# ----------------------------------------------------------------------------------

# 计算图像的边界矩形(有两种方式)
# 方法一（直边界矩形，不考虑旋转）
x, y, w, h = cv.boundingRect(
    contours2[0])                          # 获取矩形的两个对角顶点
rectangle_img = gray_img2.copy()                                    # 拷贝一份图像
cv.rectangle(rectangle_img, (x, y), (x+w, y+h), (0, 255, 0), 2)     # 在图像上画出矩形
cv.imshow("rectangle_img", rectangle_img)
# 方法二（考虑旋转，矩形面积最小）
rect = cv.minAreaRect(contours2[0])     # 获取最小矩形的两个对角顶点
box = cv.boxPoints(rect)                # 转换成四个顶点表达
box = np.int0(box)                      # 去除小数部分
min_rectangle_img = gray_img2.copy()
cv.drawContours(min_rectangle_img, [box], -1, (0, 0, 255), 2)
cv.imshow("min_rectangle_img", min_rectangle_img)

# 计算边界最小封闭圆
(x, y), radius = cv.minEnclosingCircle(contours2[0])
center = (int(x), int(y))
radius = int(radius)
circle_img = gray_img2.copy()
cv.circle(circle_img, center, radius, (0, 255, 0), 2)
cv.imshow("circle_img", circle_img)

# 计算边界的拟合椭圆
ellipse = cv.fitEllipse(contours2[0])
ellipse_img = gray_img2.copy()
cv.ellipse(ellipse_img, ellipse, (0, 255, 0), 2)
cv.imshow("ellipse_img", ellipse_img)

# 计算边界的拟合直线（没看懂原理，且不知有什么应用
rows, cols = gray_img2.shape[:2]
[vx, vy, x, y] = cv.fitLine(contours2, cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
line_img = gray_img2.copy()
cv.line(line_img, (cols-1, righty), (0, lefty), (0, 255, 0), 2)
cv.imshow("line_img", line_img)


# 销毁所有窗口
cv.waitKey()
cv.destroyAllWindows()

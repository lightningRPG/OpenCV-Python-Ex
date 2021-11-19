# coding:utf-8
# """图像边缘属性提取"""

import numpy as np
import cv2 as cv

lightning = "../pictures/ugly_lightning.png"
gray_img = cv.imread(lightning, 0)
cv.imshow("test", gray_img)
# 图像二值化
ret, thresh_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
# 提取图像边界
contours, hierarchy = cv.findContours(thresh_img, cv.INTER_AREA, cv.INTER_LINEAR)
cnt = contours[0]

# （Aspect Ratio 纵横比）图像边界矩阵的宽高比
x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h   # 示例为什么要加 float()???
print("aspect_ratio = %.4f" %(aspect_ratio))

# （Extent 范围）图像面积与其边界矩阵面积的比率
area = cv.contourArea(cnt)  
extent = float(area) / w * h
print("extent = %.4f" %(extent))

# （Solidity 稳定性）边缘面积与其凸面积的比率
hull = cv.convexHull(cnt)           # 获取凸边缘
hull_area = cv.contourArea(hull)    # 计算凸边缘的面积
solidity = float(area) / hull_area
print("solidity = %.2f" %(solidity))

# （Equivalent Diameter 等效直径）面积与边缘面积相同的圆的直径
# equi_diameter = 2 * np.sqrt(area / np.pi)
equi_diameter = np.sqrt(4 * area / np.pi)   # 与上方等价
print("equi_diameter = %.4f" %(equi_diameter))

# （Orientation 方向）边缘指向的角度
(x, y), (MA, ma), angle = cv.fitEllipse(cnt)
print("x = %d\ny = %d\nMA = %.2f\nma = %.2f\nangle = %.2f\n" 
      %(x, y, MA, ma, angle))

# （Mask and Pixel Points）啥呀这是
mask = np.zeros(gray_img.shape, np.uint8)
cv.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv.findNonZero(mask)
# 以上获取像素点的方法 cv 和 np的作用是一样的，
# 但是cv的 x，y参数 与 np是相反的，因此这里使用 np自己的方法
print("pixelpoints = %s\n" %(pixelpoints))

# （最大值和最小值以及它们的位置）使用蒙版图像找到它们位置
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray_img, mask = mask)
print("min_val = %d\nmax_val = %d\nmix_loc = %s\nmax_loc = %s\n"
      %(min_val, max_val, min_loc, max_loc))

# （Extreme Points 极点）图像上下左右最顶部的四个点
leftmost = tuple(cnt[cnt[:, :, 0]. argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0]. argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1]. argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1]. argmax()][0])
print("leftmost = %s\nrightmost = %s\ntopmost = %s\nbottommost = %s\n" 
      %(leftmost, rightmost, topmost, bottommost))


cv.waitKey()
cv.destroyAllWindows()
# Coding:UTF-8
# """图像的各种滤波"""

import cv2
import random

#
shixiongPIC = "../pictures/师兄的照片1.jpg"

#


def main():
    imgFile = "C:\\Users\\light\\Pictures\\ImageProcessing\\lena.png"
    colorImg = cv2.imread(imgFile, cv2.IMREAD_COLOR)                # 导入图像
    grayImg = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

    cv2.imshow("gray", grayImg)                                     # 展示原图
    hotPixelImg = createHotPixels(grayImg, 50000, 0.5)              # 获得噪声图片
    cv2.imshow("hotPixel", hotPixelImg)                             # 展示噪声图

    # 滤波
    blurImg = cv2.blur(hotPixelImg, (3, 3))                         # 均值滤波
    cv2.imshow("blur", blurImg)

    medianBlurImg = cv2.medianBlur(hotPixelImg, 3)                  # 中值滤波(内核的直径大小必须是奇数)
    cv2.imshow("median", medianBlurImg)

    gaussianBlurImg = cv2.GaussianBlur(hotPixelImg, (5, 5), 0)      # 高斯滤波
    cv2.imshow("gaussian", gaussianBlurImg)

    bilateralBlurImg = cv2.bilateralFilter(grayImg, 10, 20, 5)      # 双边滤波(去噪不明显，去皱纹可以有，等等...美颜！！！)
    cv2.imshow("bilateral", bilateralBlurImg)


    cv2.waitKey(-1)
    cv2.destroyAllWindows()


# 生成图像噪点
def createHotPixels(img, times=10000, chance=0.5):
    tempImg = img.copy()                                # 获得图像完全拷贝
    rows, cols = tempImg.shape                          # 获取图像宽高
    hot_pixel_times = times                             # 噪点生成判断次数
    hot_pixel_chance = 1-chance                         # 每次判断的生成概率
    # print(random.random() // hot_pixel_chance)
    for i in range(hot_pixel_times):
        if random.random() // hot_pixel_chance:         # 地板除法（直接砍去小数
            x = random.randint(0, rows-1)                 # 随机获取图像像素点xy坐标
            y = random.randint(0, cols-1)
            tempImg[x][y] = random.randint(0, 256)      # 像素点随机赋值(模拟噪点)

    return tempImg                                      # 输出图像


# 启动主程序
if __name__ == '__main__': main()


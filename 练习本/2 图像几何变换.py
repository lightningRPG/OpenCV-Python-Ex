# coding: utf-8
# """图像的集合变换"""

import numpy as np
import cv2 as cv

lena = "../pictures/lena.png"
color_img = cv.imread(lena, cv.IMREAD_COLOR)
gray_img = cv.imread(lena, cv.IMREAD_GRAYSCALE)
ROWS, COLS = gray_img.shape                 # 实验图像的宽高
CENTER = ((ROWS-1)/2.0, (COLS-1)/2.0)       # 实验图像的中心点


def main():
    # 需要看哪个就解掉注释
    if (test_scaling()): print("图像等比缩放")
        
    if (test_translation()): print("图像平移")
        
    if (test_rotation()): print("图像旋转")
        
    else: print("没有启动任何测试")

    print("<<测试结束>>")
    
    return


# 等比例缩放
def test_scaling():
    scaling_img = cv.resize(color_img, None, fx=2, fy=0.5, interpolation=cv.INTER_CUBIC)
    cv.imshow("Color", color_img)
    cv.imshow("Scaling", scaling_img)
    cv.waitKey()
    
    return True
    

# 平移
def test_translation():
    M = np.float32([[1, 0, 100], [0, 1, 200]])  # 第三个元素是平移距离
    # M = cv.getRotationMatrix2D((CENTER[0]+100, CENTER[1]-50), 90, 1)
    translation_img = cv.warpAffine(color_img, M, (ROWS, COLS))
    cv.imshow("Color", color_img)
    cv.imshow("Translation", translation_img)
    cv.waitKey()

    return True


# 旋转
    """
        此方法还能顺带平移，但不能单独用于平移
        可以单独用于等比缩放
    """
def test_rotation():
    M = cv.getRotationMatrix2D(CENTER, 180, 2)
    rotation_img = cv.warpAffine(color_img, M, (ROWS, COLS))
    cv.imshow("Color", color_img)
    cv.imshow("Rotation", rotation_img)
    cv.waitKey()
    
    return True





if __name__ == '__main__':
    main()

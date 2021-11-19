# coding:utf-8
# coding:cp936
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\light\Pictures\ImageProcessing\OIP-C.png")
cv2.namedWindow("cs")
cv2.imshow("cs", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# coding:utf-8
# """边缘 Contours 的层次结构分析"""

import cv2 as cv

# black and white picture
bwpic = "../pictures/bwframes.jpg"
gray_img = cv.imread(bwpic, 2)
ret, thresh_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
cv.imshow("look at this", thresh_img)

# 返回值 hierarchy 和 cv.RETR_... 有关，其中包含了每条边缘的层次关系
# hierarchy 是一个嵌套数组其中每个最小单位代表 
# [Next, Previous, First_Child, Parent] -> [同层下一条边缘, 同层上一条边缘, 第一条子边缘, 所属父边缘]
img1 = thresh_img.copy()
# cv.RETR_LIST 给出所有边缘的同层顺序关系，忽略包含关系（无或者忽略则为 -1）
contours1, list_hierarchy = cv.findContours(img1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

img2 = thresh_img.copy()
# cv.RETR_EXTERNAL 给出最外层级所有边缘的顺序关系
contours2, external_hierarchy = cv.findContours(img2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

img3 = thresh_img.copy()
# cv.RETR_CCOMP 按每个物体分，边缘层级分为两层，第一二层分别代表外内轮廓，从里往外排
contours3, ccomp_hierarchy = cv.findContours(img3, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

img4 = thresh_img.copy()
# cv.RETR_TREE 明确给出每条边缘的完整层级关系（非常推荐，平时用它就对了！）
contours4, tree_hierarchy = cv.findContours(img4, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


# if (contours1 == contours4): print("好耶")
print(list_hierarchy,'\n')
print(external_hierarchy, '\n')
print(ccomp_hierarchy, '\n')
print(tree_hierarchy, '\n')
print('---------------------------------------------------')
print(contours1, '\n')


cv.waitKey()
cv.destroyAllWindows()
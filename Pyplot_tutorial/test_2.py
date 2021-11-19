# coding:utf-8

from matplotlib import pyplot as plt
import numpy as np

data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)
}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(16, 8))     # 设置之后的表格的xy轴初始值（表格中的数据会撑大表格
plt.plot([1, 2, 100], 'ro')  # 无论多少个数都是
plt.show()    # 此表为体现figure函数的变化
# 每次调用show()都会重置plt其他函数对图表的更改!!!
"""
    subplot的三个参数解释：
        前两个参数是相对整个白板的行列划分
        第一个是行数，第二个是列数，第三个参数是自身所占其中的索引数
        顺序从左往右，从上到下
"""    
plt.figure(figsize=(16, 8))
plt.subplot(231)        # 完整写法：plt.subplot(1, 3, 1)
plt.bar(names, values)                  # 使图像柱状显示

plt.subplot(234)        # 分别表示：本列图像行数，总共列数，所占第几列数
plt.scatter(names, values)              # 使图像点状显示

plt.subplot(133)
plt.plot(names, values)                 # 使图像线状显示

plt.suptitle('Categorical Plotting')    # 顶部的总标题
plt.show()

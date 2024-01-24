import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import json

# 初始化差异列表
differences = []

# 读取并处理图像0.png，将其作为参考图像
ref_img = cv2.imread('0.png', cv2.IMREAD_GRAYSCALE)
_, ref_img = cv2.threshold(ref_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
ref_contours, _ = cv2.findContours(ref_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ref_cnt = max(ref_contours, key=cv2.contourArea)

# 初始化形状上下文描述符计算器
sd = cv2.createShapeContextDistanceExtractor()

# 初始化一个 40*40 的零矩阵
matrix = [[0 for _ in range(40)] for _ in range(40)]

# 循环处理图像1.png到39.png
for i in range(1, 40):
    # 读取并处理图像
    img = cv2.imread(f'{i}.png', cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)

    # 计算形状上下文描述符，并将结果添加到列表中
    match = sd.computeDistance(ref_cnt, cnt)

    # 计算形状上下文描述符，并将结果存入矩阵的第一列
    match = sd.computeDistance(ref_cnt, cnt)
    matrix[0][i] = match
    matrix[i][0] = match
    # differences.append(match)
    # differences.append({"image": i, "difference": match})

# 将结果保存为json
with open('matrix2.json', 'w') as f:
    json.dump(matrix, f)

# # 创建平滑的曲线数据
# x = np.arange(1, 40)
# spl = make_interp_spline(x, differences)
# x_smooth = np.linspace(x.min(), x.max(), 500)
# y_smooth = spl(x_smooth)
#
# # 绘制结果
# plt.plot(x_smooth, y_smooth)
# plt.xlabel('图片序号')
# plt.ylabel('形状上下文距离')
# plt.show()
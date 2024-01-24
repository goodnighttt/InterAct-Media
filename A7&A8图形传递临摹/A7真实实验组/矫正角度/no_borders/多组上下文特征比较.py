import cv2
import numpy as np
import matplotlib.pyplot as plt

# 初始化差异列表
differences = []

# 读取并处理图像0.png，将其作为参考图像
ref_img = cv2.imread('1__no_borders.png', cv2.IMREAD_GRAYSCALE)
_, ref_img = cv2.threshold(ref_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
ref_contours, _ = cv2.findContours(ref_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ref_cnt = max(ref_contours, key=cv2.contourArea)

# 初始化形状上下文描述符计算器
sd = cv2.createShapeContextDistanceExtractor()

# 循环处理图像1.png到39.png
for i in range(2, 40):
    # 读取并处理图像
    img = cv2.imread(f'{i}__no_borders.png', cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)

    # 计算形状上下文描述符，并将结果添加到列表中
    match = sd.computeDistance(ref_cnt, cnt)
    differences.append(match)

print(differences)
# 绘制结果
plt.plot(differences)
plt.xlabel('Image Number')
plt.ylabel('Shape Context Distance')
plt.show()

import cv2
import numpy as np

# 读取图像并转为灰度图
img1 = cv2.imread('0.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('5.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, img1 = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, img2 = cv2.threshold(img2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 找到图像的轮廓
contours1, _ = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 计算形状上下文描述符
sd = cv2.createShapeContextDistanceExtractor()
# 选择两个最大的轮廓进行比较
cnt1 = max(contours1, key=cv2.contourArea)
cnt2 = max(contours2, key=cv2.contourArea)
match = sd.computeDistance(cnt1, cnt2)

print(match)

# 创建一个空白的图像用于绘制轮廓
blank_img1 = np.zeros_like(img1)
blank_img2 = np.zeros_like(img2)

# 绘制轮廓
cv2.drawContours(blank_img1, contours1, -1, (255), 1)
cv2.drawContours(blank_img2, contours2, -1, (255), 1)

# 显示图像
cv2.imshow('Contours1', blank_img1)
cv2.imshow('Contours2', blank_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
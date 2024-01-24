import cv2

# 加载图像并转换为灰度图像
image = cv2.imread('image/1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用边缘检测算法
edges = cv2.Canny(gray, 50, 150)  # 设置阈值参数为50和150

# 轮廓检测
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 选择整个字的外轮廓
# 这里可以根据轮廓的面积、长度等属性来筛选出整个字的轮廓

# 绘制轮廓
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# 显示结果
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

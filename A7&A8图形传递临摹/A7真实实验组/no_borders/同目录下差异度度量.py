import os
import glob
import cv2
from PIL import Image
import numpy as np
from skimage import img_as_float
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 读取图像并将其转换为浮点数组的函数
def load_image(image_path):
    return img_as_float(np.array(Image.open(image_path).convert("L")))

# 计算图像的重心
def calculate_centroid(img):
    y, x = np.where(img > 0)
    return np.mean(x), np.mean(y)

# 计算图像的梯度方向
def calculate_gradient_direction(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    gradient_direction = np.arctan2(sobely, sobelx)
    return gradient_direction

# 计算加权总差异
def calculate_difference(img1, img2):
    # 图像像素差异
    img1_float = img_as_float(img1)
    img2_float = img_as_float(img2)
    pixel_diff = np.sum(np.abs(img1_float - img2_float))

    # 重心差异
    centroid_diff = np.linalg.norm(np.array(calculate_centroid(img1)) - np.array(calculate_centroid(img2)))

    # 梯度方向差异
    # gradient_direction_diff = np.sum(np.abs(calculate_gradient_direction(img1) - calculate_gradient_direction(img2)))
    gradient_direction_diff = np.sum(np.abs(calculate_gradient_direction(img1))) - np.sum(np.abs(calculate_gradient_direction(img2)))

    # 返回每种差异度
    return pixel_diff, centroid_diff, gradient_direction_diff
    # # 通过加权方式计算最终的差异度
    # # 这里的权重可以根据实际需要进行调整
    # total_diff = 0.2 * pixel_diff + 0.3 * centroid_diff + 0.5 * gradient_direction_diff
    #
    # return total_diff



# 指定图像文件的目录
image_dir = './'

# 获取目录下所有png文件的路径
image_files = glob.glob(os.path.join(image_dir, "*_no_borders.png"))

import re

# 提取文件名中的数字
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

# 按数字排序
image_files.sort(key=extract_number)

# # 按文件名排序，这样编号0的图片会在第一个
# image_files.sort()

# 加载编号0的图片
img_0 = load_image(image_files[0])


# 初始化列表，用于存储差异度
differences = []
pixel_diffs = []
centroid_diffs = []
gradient_diffs = []

# 对每一张除0之外的图片进行处理
for image_file in image_files[1:]:
    # 加载图片
    img = load_image(image_file)
    # 计算差异度并添加到列表中
    # differences.append(calculate_difference(img_0, img))
    pixel_diff, centroid_diff, gradient_diff = calculate_difference(img_0, img)
    pixel_diffs.append(pixel_diff)
    centroid_diffs.append(centroid_diff)
    gradient_diffs.append(gradient_diff)

# 对每种差异度进行归一化
pixel_diffs = (pixel_diffs - np.min(pixel_diffs)) / (np.max(pixel_diffs) - np.min(pixel_diffs))
centroid_diffs = (centroid_diffs - np.min(centroid_diffs)) / (np.max(centroid_diffs) - np.min(centroid_diffs))
gradient_diffs = (gradient_diffs - np.min(gradient_diffs)) / (np.max(gradient_diffs) - np.min(gradient_diffs))

print(pixel_diffs)
print(centroid_diffs)
print(gradient_diffs)

# 计算总差异度
# total_diffs = 0.5 * pixel_diffs + 0.3 * centroid_diffs + 0.2 * gradient_diffs
total_diffs = 0.4 * pixel_diffs + 0.3 * centroid_diffs + 0.3 * gradient_diffs

# 创建x轴的值（图片的编号）
x = range(1, len(image_files))

# 使用make_interp_spline创建平滑的折线
spl = make_interp_spline(x, total_diffs)
x_smooth = np.linspace(min(x), max(x), 500)
y_smooth = spl(x_smooth)

# 绘制平滑的折线图
plt.plot(x_smooth, y_smooth)
plt.xlabel('Image number')
plt.ylabel('Difference from image 0')
plt.title('Difference from image 0 over time')
plt.show()

# # 创建x轴的值（图片的编号）
# x = range(1, len(image_files))
#
# # 使用make_interp_spline创建平滑的折线
# spl = make_interp_spline(x, differences)
# x_smooth = np.linspace(min(x), max(x), 500)
# y_smooth = spl(x_smooth)
#
# # 绘制平滑的折线图
# plt.plot(x_smooth, y_smooth)
# plt.xlabel('Image number')
# plt.ylabel('Difference from image 0')
# plt.title('Difference from image 0 over time')
# plt.show()

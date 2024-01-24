import os
import glob
import cv2
from PIL import Image
import numpy as np
from skimage import img_as_float
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


# 初始化形状上下文描述符计算器
sd = cv2.createShapeContextDistanceExtractor()

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

def calculate_ShapeContext_Distance(img):
    # img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img = cv2.convertScaleAbs(img)  # 转换为8位图像
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)
    return cnt

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

    # 形状上下文差异
    # shape_context_diff = sd.computeDistance(calculate_ShapeContext_Distance(img1), calculate_ShapeContext_Distance(img2))

    # 返回每种差异度
    return pixel_diff, centroid_diff, gradient_direction_diff
        # , shape_context_diff
    # # 通过加权方式计算最终的差异度
    # # 这里的权重可以根据实际需要进行调整
    # total_diff = 0.2 * pixel_diff + 0.3 * centroid_diff + 0.5 * gradient_direction_diff
    #
    # return total_diff



# 指定图像文件的目录
image_dir = './'

# 获取目录下所有png文件的路径
image_files = glob.glob(os.path.join(image_dir, "*__no_borders.png"))

import re

# 提取文件名中的数字
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

# 按数字排序
image_files.sort(key=extract_number)

# print(image_files)

# 加载编号0的图片
img_0 = load_image(image_files[0])


# 初始化列表，用于存储差异度
differences = []
pixel_diffs = []
centroid_diffs = []
gradient_diffs = []
shape_context_diffs = []

# 读取并处理图像0.png，将其作为参考图像
ref_img = cv2.imread('1__no_borders.png', cv2.IMREAD_GRAYSCALE)
_, ref_img = cv2.threshold(ref_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
ref_contours, _ = cv2.findContours(ref_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ref_cnt = max(ref_contours, key=cv2.contourArea)

for i in range(2, 40):
    # 读取并处理图像
    img = cv2.imread(f'{i}__no_borders.png', cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)

    # 计算形状上下文描述符，并将结果添加到列表中
    match = sd.computeDistance(ref_cnt, cnt)
    shape_context_diffs.append(match)
# print(shape_context_diffs)


# 对每一张除0之外的图片进行处理
for image_file in image_files[1:]:
    # 加载图片
    print(image_file)
    img = load_image(image_file)
    # 计算差异度并添加到列表中
    # differences.append(calculate_difference(img_0, img))
    pixel_diff, centroid_diff, gradient_diff = calculate_difference(img_0, img)
    pixel_diffs.append(pixel_diff)
    centroid_diffs.append(centroid_diff)
    gradient_diffs.append(gradient_diff)
    # shape_context_diffs.append(shape_context_diff)
    # print(shape_context_diffs)

# print(shape_context_diffs)
# 对每种差异度进行归一化
pixel_diffs = (pixel_diffs - np.min(pixel_diffs)) / (np.max(pixel_diffs) - np.min(pixel_diffs))
centroid_diffs = (centroid_diffs - np.min(centroid_diffs)) / (np.max(centroid_diffs) - np.min(centroid_diffs))
gradient_diffs = (gradient_diffs - np.min(gradient_diffs)) / (np.max(gradient_diffs) - np.min(gradient_diffs))
shape_context_diffs = (shape_context_diffs - np.min(shape_context_diffs)) / (np.max(shape_context_diffs) - np.min(shape_context_diffs))

print(pixel_diffs)
print(centroid_diffs)
print(gradient_diffs)
print(shape_context_diffs)

# 计算总差异度
# total_diffs = 0.5 * pixel_diffs + 0.3 * centroid_diffs + 0.2 * gradient_diffs
# total_diffs = 0.15 * pixel_diffs + 0.35 * gradient_diffs + 0.5 * shape_context_diffs
total_diffs = 0.15 * pixel_diffs + 0.35 * gradient_diffs + 0.5 * shape_context_diffs
total_diffs = (total_diffs - np.min(total_diffs)) / (np.max(total_diffs) - np.min(total_diffs))



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

# 创建一个字典，用于存储每种差异度
diff_dict = {
    'pixel_diffs': list(pixel_diffs),
    # 'centroid_diffs': list(centroid_diffs),
    'gradient_diffs': list(gradient_diffs),
    'shape_context_diffs': list(shape_context_diffs),
    'total_diffs': list(total_diffs)
}

# 创建一个列表，用于存储每张图片的信息
image_data = []
for i, image_file in enumerate(image_files[1:], start=1):
    image_data.append({
        'image_number': i,
        'image_name': os.path.basename(image_file),
        'pixel_diff': diff_dict['pixel_diffs'][i-1],
        # 'centroid_diff': diff_dict['centroid_diffs'][i-1],
        'gradient_diff': diff_dict['gradient_diffs'][i-1],
        'shape_context_diff': diff_dict['shape_context_diffs'][i-1],
        'total_diff': diff_dict['total_diffs'][i-1]
    })

#
# import csv
#
# # 数据的列标题
# column_names = ['image_number', 'image_name', 'pixel_diff', 'gradient_diff', 'shape_context_diff', 'total_diff']
#
# # 创建一个新的CSV文件
# with open('image_diff_data.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=column_names)
#
#     # 写入标题
#     writer.writeheader()
#
#     # 写入数据
#     for data in image_data:
#         writer.writerow(data)


import json



# 将数据保存为json
with open('image_diff_data.json', 'w') as f:
    json.dump(image_data, f, indent=4)


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

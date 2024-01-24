import json
import numpy as np

# 读取json文件
with open('image_diff_data.json', 'r') as f:
    image_data = json.load(f)

# 获取图像数量
num_images = len(image_data) + 1  # +1是为了包括第一幅图像

# 初始化四个矩阵为全零
pixel_diff_matrix = np.zeros((num_images, num_images))
total_diff_matrix = np.zeros((num_images, num_images))
gradient_diff_matrix = np.zeros((num_images, num_images))
shape_context_diff_matrix = np.zeros((num_images, num_images))

# 填充矩阵
for data in image_data:
    i = data['image_number']
    pixel_diff_matrix[0, i] = data['pixel_diff']
    pixel_diff_matrix[i, 0] = data['pixel_diff']

    total_diff_matrix[0, i] = data['total_diff']
    total_diff_matrix[i, 0] = data['total_diff']

    gradient_diff_matrix[0, i] = data['gradient_diff']
    gradient_diff_matrix[i, 0] = data['gradient_diff']

    shape_context_diff_matrix[0, i] = data['shape_context_diff']
    shape_context_diff_matrix[i, 0] = data['shape_context_diff']

import json

# 准备用于存储在 JSON 文件中的字典
json_data = {
    'pixel_diff_matrix': pixel_diff_matrix.tolist(),
    'total_diff_matrix': total_diff_matrix.tolist(),
    'gradient_diff_matrix': gradient_diff_matrix.tolist(),
    'shape_context_diff_matrix': shape_context_diff_matrix.tolist(),
}

# 将字典保存为 JSON 文件
with open('image_diff_matrices.json', 'w') as f:
    json.dump(json_data, f, indent=4)

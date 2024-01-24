import cv2
import numpy as np
from PIL import Image
import os

def remove_black_borders(image_path, output_path, border_size=40):
    # 加载图片
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 找到所有非黑色像素的坐标
    coords = np.column_stack(np.where(img > 0))

    # 计算非黑色像素的最小和最大坐标值
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    # 对图像进行裁剪
    img_no_borders = img[y_min:y_max+1, x_min:x_max+1]

    # 将裁剪后的图像转为PIL Image，以便进行resize操作
    img_no_borders = Image.fromarray(img_no_borders)

    # 进行resize操作，将图像大小变为1024*1024像素
    img_no_borders = img_no_borders.resize((256 - 2 * border_size, 256 - 2 * border_size), Image.ANTIALIAS)

    # 创建一个新的空白图片（大小为256*256，颜色为黑色）
    new_img = Image.new('L', (256, 256))

    # 将去除黑边后的图片粘贴到新的空白图片中间，从而形成一个黑色边框
    new_img.paste(img_no_borders, (border_size, border_size))

    # 再次进行二值化操作
    new_img = new_img.point(lambda x: 0 if x<128 else 255)

    # 转换图像颜色模式并保存
    new_img = np.array(new_img, dtype='uint8')
    cv2.imwrite(output_path, new_img)


# def remove_black_borders(image_path, output_path):
#     # 加载图片
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#
#     # 找到所有非黑色像素的坐标
#     coords = np.column_stack(np.where(img > 0))
#
#     # 计算非黑色像素的最小和最大坐标值
#     y_min, x_min = coords.min(axis=0)
#     y_max, x_max = coords.max(axis=0)
#
#     # 对图像进行裁剪
#     img_no_borders = img[y_min:y_max+1, x_min:x_max+1]
#
#     # 将裁剪后的图像转为PIL Image，以便进行resize操作
#     img_no_borders = Image.fromarray(img_no_borders)
#
#     # 进行resize操作，将图像大小变为1024*1024像素
#     img_no_borders = img_no_borders.resize((256, 256), Image.ANTIALIAS)
#
#     # 转换图像模式为'L'
#     img_no_borders = img_no_borders.convert('L')
#
#     # 再次进行二值化操作
#     img_no_borders = img_no_borders.point(lambda x: 0 if x<128 else 255)
#
#     # 转换图像颜色模式并保存
#     img_no_borders = np.array(img_no_borders, dtype='uint8')
#     cv2.imwrite(output_path, img_no_borders)

# 定义你的目录路径
directory_path = './'

# 遍历目录下的所有文件
for filename in os.listdir(directory_path):
    # 检查文件是否为图片（这里仅检查文件名是否以.png结尾）
    if filename.endswith('.png'):
        image_path = os.path.join(directory_path, filename)
        output_path = os.path.join(directory_path, 'no_borders', filename.replace('.png', '_no_borders.png'))
        remove_black_borders(image_path, output_path)

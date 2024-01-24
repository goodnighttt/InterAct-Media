import cv2
import numpy as np
from PIL import Image

def remove_black_borders(image_path, output_path):
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
    img_no_borders = img_no_borders.resize((1024, 1024), Image.ANTIALIAS)

    # 保存图像
    cv2.imwrite(output_path, np.array(img_no_borders))

# 调用函数
remove_black_borders('11.png', '11_no_borders.png')

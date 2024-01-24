import cv2
from PIL import Image
import numpy as np

def binarize_image(image_path, output_path, threshold=100):
    # 读取图像并转为灰度图
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 创建二值图像，像素值低于阈值的区域被标记为255（白色），其余区域标记为0（黑色）
    binary = np.where(gray < threshold, 255, 0).astype('uint8')

    # 将二值图像保存为一张新的图片
    Image.fromarray(binary).save(output_path)

# 你的图片路径
image_path = "A8-1.jpg"
# 你希望存储二值化后的图片路径
output_path = "A8-1_binary.png"

binarize_image(image_path, output_path)

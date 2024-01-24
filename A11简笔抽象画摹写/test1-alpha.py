import cv2
import numpy as np
import os

# 读取图像文件夹中的所有图像文件
image_folder = './image'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

# 按文件名排序图像文件
images.sort(key=lambda x: int(x.split('.')[0]))

# 读取第一个图像作为基准图像
base_image = cv2.imread(os.path.join(image_folder, images[0]))

# 创建输出视频对象
output_video = cv2.VideoWriter('输出视频文件.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (base_image.shape[1], base_image.shape[0]))

# 对于每个图像文件
for i in range(1, len(images)):
    # 读取当前图像
    current_image = cv2.imread(os.path.join(image_folder, images[i]))

    # 图像间的平滑过渡
    for alpha in np.linspace(0, 1, 10):
        # 通过线性插值创建中间图像
        interpolated_image = cv2.addWeighted(base_image, 1 - alpha, current_image, alpha, 0)

        # 在视频中写入中间图像
        output_video.write(interpolated_image)

        # 显示中间图像
        cv2.imshow('Morphing', interpolated_image)
        cv2.waitKey(1)

    # 设置下一个基准图像
    base_image = current_image

# 释放视频对象和窗口
output_video.release()
cv2.destroyAllWindows()

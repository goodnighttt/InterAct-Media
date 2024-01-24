import cv2
import numpy as np
import os
from scipy.spatial import Delaunay

def calculate_affine_transform(source_points, target_points):
    """
    计算仿射变换矩阵
    """
    assert len(source_points) == len(target_points) >= 3

    source_tri = np.float32(source_points)
    target_tri = np.float32(target_points)

    return cv2.getAffineTransform(source_tri, target_tri)

def warp_image(source_image, source_points, target_points):
    """
    图像形状变形
    """
    affine_transform = calculate_affine_transform(source_points, target_points)
    warped_image = cv2.warpAffine(source_image, affine_transform, (source_image.shape[1], source_image.shape[0]))

    return warped_image

def select_feature_points(image, num_points):
    """
    手动选择特征点
    """
    points = []
    win_name = 'Select Feature Points'

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
            cv2.imshow(win_name, image)

    cv2.namedWindow(win_name)
    cv2.setMouseCallback(win_name, mouse_callback)

    while len(points) < num_points:
        cv2.imshow(win_name, image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyWindow(win_name)

    return points

# 读取图像文件夹中的所有图像文件
image_folder = './image'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

# 按文件名排序图像文件
images.sort(key=lambda x: int(x.split('.')[0]))

# 读取第一个图像作为基准图像
base_image = cv2.imread(os.path.join(image_folder, images[0]))

# 手动选择基准图像的特征点
base_points = np.array(select_feature_points(base_image, num_points=10), dtype=np.int32)

# 中间图像的数量（包括基准图像和最后一张图像）
num_intermediate_images = 5

# 创建输出视频对象
output_video = cv2.VideoWriter('输出视频文件.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (base_image.shape[1], base_image.shape[0]))

# 对于每个图像文件
for i in range(1, len(images)):
    # 读取当前图像
    current_image = cv2.imread(os.path.join(image_folder, images[i]))

    # 手动选择当前图像的特征点
    current_points = np.array(select_feature_points(current_image, num_points=10), dtype=np.int32)

    # 进行Delaunay三角剖分
    tri = Delaunay(base_points)
    triangles = tri.simplices.astype(int)

    # 在每个三角形上进行形状变形
    for alpha in np.linspace(0, 1, num_intermediate_images):
        # 创建中间图像的特征点
        intermediate_points = alpha * current_points + (1 - alpha) * base_points

        # 在每个三角形上进行形状变形
        for triangle in triangles:
            # 提取基准图像和当前图像的特征点
            base_triangle = base_points[triangle]
            current_triangle = current_points[triangle]
            intermediate_triangle = intermediate_points[triangle]

            # 进行形状变形
            warped_image = warp_image(base_image, base_triangle, intermediate_triangle)

            # 在视频中写入变形后的图像
            output_video.write(warped_image)

            # 显示变形后的图像
            cv2.imshow('Shape Warping', warped_image)
            cv2.waitKey(1)

    # 设置下一个基准图像和特征点
    base_image = current_image
    base_points = current_points

# 释放视频对象和窗口
output_video.release()
cv2.destroyAllWindows()

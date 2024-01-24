import cv2
import numpy as np

# 加载三张文字图片
image1 = cv2.imread('image/1.jpg')
image2 = cv2.imread('image/2.jpg')
image3 = cv2.imread('image/3.jpg')

# 转换为灰度图像
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges1 = cv2.Canny(gray1, 50, 150)
edges2 = cv2.Canny(gray2, 50, 150)
edges3 = cv2.Canny(gray3, 50, 150)

# 查找轮廓
contours1, _ = cv2.findContours(edges1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(edges2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours3, _ = cv2.findContours(edges3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 寻找对应边缘
matched_pairs = []
for contour1 in contours1:
    best_match = None
    best_score = float('inf')
    for contour2 in contours2:
        score = cv2.matchShapes(contour1, contour2, cv2.CONTOURS_MATCH_I1, 0)
        if score < best_score:
            best_score = score
            best_match = contour2
    if best_match is not None:
        matched_pairs.append((contour1, best_match))

# 定义过渡帧数量
num_frames = 10

# 创建输出视频对象
output_video = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (image1.shape[1], image1.shape[0]))

# 生成过渡帧
for i in range(num_frames + 1):
    # 计算当前帧的权重
    alpha = i / num_frames

    # 使用权重生成过渡帧
    transition_image = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)

    # 在过渡帧上绘制对应边缘
    for contour1, contour2 in matched_pairs:
        contour = cv2.approxPolyDP(contour1, 3, True)
        for point in contour:
            x, y = point[0]
            cv2.circle(transition_image, (x, y), 3, (0, 0, 255), -1)

    # 写入输出视频
    output_video.write(transition_image)

    # 显示过渡帧
    cv2.imshow('Transition', transition_image)
    cv2.waitKey(30)

# 清空匹配对
matched_pairs = []

# 寻找第二对对应边缘
for contour2 in contours2:
    best_match = None
    best_score = float('inf')
    for contour3 in contours3:
        score = cv2.matchShapes(contour2, contour3, cv2.CONTOURS_MATCH_I1, 0)
        if score < best_score:
            best_score = score
            best_match = contour3
    if best_match is not None:
        matched_pairs.append((contour2, best_match))

# 生成第二段过渡帧
for i in range(num_frames + 1):
    # 计算当前帧的权重
    alpha = i / num_frames

    # 使用权重生成过渡帧
    transition_image = cv2.addWeighted(image2, 1 - alpha, image3, alpha, 0)

    # 在过渡帧上绘制对应边缘
    for contour2, contour3 in matched_pairs:
        contour = cv2.approxPolyDP(contour3, 3, True)
        for point in contour:
            x, y = point[0]
            cv2.circle(transition_image, (x, y), 3, (0, 0, 255), -1)

    # 写入输出视频
    output_video.write(transition_image)

    # 显示过渡帧
    cv2.imshow('Transition', transition_image)
    cv2.waitKey(30)

# 释放视频对象和窗口
output_video.release()
cv2.destroyAllWindows()

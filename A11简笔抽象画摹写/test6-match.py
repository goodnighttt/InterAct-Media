import cv2
import numpy as np

def detect_edges(image):
    # 使用Canny边缘检测算法
    edges = cv2.Canny(image, 50, 150)
    return edges

def extract_features(image):
    # 使用SIFT算法提取特征点和描述符
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors

def match_features(descriptors1, descriptors2):
    # 使用FLANN匹配器进行特征匹配
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    # 应用比例测试，筛选出最佳匹配
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    return good_matches

# 加载图片
image1 = cv2.imread('image/1.jpg')
image2 = cv2.imread('image/2.jpg')

# 边缘检测
edges1 = detect_edges(image1)
edges2 = detect_edges(image2)

# 特征提取和匹配
keypoints1, descriptors1 = extract_features(edges1)
keypoints2, descriptors2 = extract_features(edges2)
matches = match_features(descriptors1, descriptors2)

# 可视化匹配结果
output_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches, None)
cv2.imshow('Matches', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

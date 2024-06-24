import os
import numpy as np
from sklearn.cluster import KMeans
import cv2
import shutil
#kmaens 聚类分类
def kmeans_segmentation(image_path, k):
    # 读取图像
    image = cv2.imread(image_path)

    # 转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 将图像数据转换为一维数组
    flattened_image = gray_image.reshape((-1, 1))

    # 使用K-means算法进行聚类
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, tol=1e-4)
    kmeans.fit(flattened_image)

    # 获取每个像素的标签
    labels = kmeans.labels_

    # 将标签重新组织为与原始图像相同形状的二维数组
    segmented_image = labels.reshape(gray_image.shape)

    # 根据分割结果，用0、128、255作为三个类别的像素值
    segmented_image[segmented_image == 0] = 0
    segmented_image[segmented_image == 1] = 128
    segmented_image[segmented_image == 2] = 255

    # 计算每个聚类的平均像素值
    cluster_centers = kmeans.cluster_centers_.flatten()

    # 显示每个聚类的平均像素值
    for i, center in enumerate(cluster_centers):
        print("Cluster", i+1, "Mean Pixel Value:", center)

    # 将数据类型转换为uint8
    segmented_image = segmented_image.astype(np.uint8)

    # 返回分割后的图像
    return segmented_image

# 设置图像路径和聚类数目

image_path = r"C:\pythonProject2\cat\683.jpg"
k = 3

# 调用kmeans_segmentation()函数进行图像分割，并将结果保存在变量segmented_image中
segmented_image = kmeans_segmentation(image_path, k)

# 展示分割后的图像
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

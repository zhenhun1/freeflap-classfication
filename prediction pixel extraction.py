import os
import cv2
import random
import pandas as pd
import numpy as np

# 设置输入和输出文件夹
image_dir = r'D:\2'
output_dir = r'D:\2\output'
mask_dir = r'D:\2\masks'  # 掩膜文件夹
os.makedirs(output_dir, exist_ok=True)

# 读取目录下的文件名
image_filenames = os.listdir(image_dir)

# 筛选出所有的png和jpg文件
valid_extensions = ['.png', '.jpg']
image_filenames = [f for f in image_filenames if os.path.splitext(f)[1].lower() in valid_extensions]

for image_filename in image_filenames:
    try:
        # 构造原始图像路径和掩膜路径
        image_path = os.path.join(image_dir, image_filename)
        mask_path = os.path.join(mask_dir, image_filename)

        # 读取原始图像和掩膜图像并灰度化
        original_image = cv2.imread(image_path, 0)
        mask_image = cv2.imread(mask_path, 0)
        if original_image is None or mask_image is None:
            print(f"无法加载图像或掩膜: {image_path} 或 {mask_path}")
            continue

        # 创建彩色画布并复制灰度化的原始图像
        canvas = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)

        # 存储像素值的列表
        line_pixel_values = []

        # 绘制的直线数目
        line_count = 0
        max_attempts = 1000  # 设置最大尝试次数以避免无限循环
        attempts = 0

        while line_count < 14 and attempts < max_attempts:
            # 随机选择一个纵坐标
            random_coordinate = random.randint(0, original_image.shape[0] - 1)

            # 获取该行的像素值和掩膜值
            row = original_image[random_coordinate, :]
            mask_row = mask_image[random_coordinate, :]

            # 检查是否有超过120个像素值为0且掩膜行包含128和255两个值
            if np.count_nonzero(row == 0) > 120 or not (128 in mask_row and 255 in mask_row):
                attempts += 1
                continue

            # 将像素值添加到列表中
            line_pixel_values.append([line_count] + row.tolist())

            # 在画布上绘制红色直线
            cv2.line(canvas, (0, random_coordinate), (original_image.shape[1] - 1, random_coordinate), (0, 0, 255), 1)

            # 绘制直线数目加一
            line_count += 1

        if line_count < 14:
            print(f"无法找到足够的有效线条用于图像: {image_path}")
            continue

        # 将像素值存入DataFrame
        columns = ['line_number'] + [f'pixel_{i}' for i in range(original_image.shape[1])]
        df = pd.DataFrame(line_pixel_values, columns=columns)

        # 生成与源图像名字一致的保存文件名
        output_filename = image_filename.split('.')[0] + '_test.xlsx'
        output_path = os.path.join(output_dir, output_filename)
        df.to_excel(output_path, index=False)

        # 生成与源图像名字一致的保存文件名
        canvas_filename = image_filename.split('.')[0] + '_canvas.jpg'
        canvas_path = os.path.join(output_dir, canvas_filename)
        cv2.imwrite(canvas_path, canvas)

    except Exception as e:
        print(f"处理图像 {image_filename} 时出错: {e}")

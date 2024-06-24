import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# 读取Excel文件

data = pd.read_excel(r'C:\新建文件夹\DATA\train\ma.xlsx', engine='openpyxl')
# 获取标签列和数据列
labels = data.iloc[:, 0]
values = data.iloc[:, 1:226]  # 假设数据从第二列到第226列

# 对每行数据进行移动平均处理
window_size = 3  # 设置窗口大小
values_smoothed = values.rolling(window_size, min_periods=1).mean()

# 遍历每一行数据，提取特征并导出到Excel文件
results = pd.DataFrame(columns=['标签', '波峰', '波谷', '标准差', '波谷间距特征'])   #只用到了标准差，波谷间距特征
for i in range(len(labels)):
    peaks, _ = find_peaks(values_smoothed.iloc[i, :].values)
    valleys, _ = find_peaks(-values_smoothed.iloc[i, :].values)

    # 选择较少的峰值或谷值进行计算，并确保它们具有相同的长度
    if len(peaks) < len(valleys):
        selected_peaks = peaks
        selected_valleys = valleys[:len(peaks)]
    else:
        selected_peaks = peaks[:len(valleys)]
        selected_valleys = valleys

    std = np.std(selected_peaks - selected_valleys)

    # 计算波谷间距特征
    valley_distances = np.diff(selected_valleys)  # 计算波谷之间的距离
    valley_distances_std = np.std(valley_distances) if len(valley_distances) > 0 else 0

    results.loc[len(results)] = [labels.iloc[i], len(selected_peaks), len(selected_valleys), std, valley_distances_std]

# 将结果导出到Excel文件
results.to_excel(r'C:\新建文件夹\DATA\train\ma3.xlsx', index=False)

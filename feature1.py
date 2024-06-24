import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# 读取Excel文件
df = pd.read_excel(r'C:\新建文件夹\DATA\train\ma.xlsx', engine='openpyxl')

# 提取标签和数据列
labels = df.iloc[:, 0]
data = df.iloc[:, 1:]

# 用于存储特征的列表
std_list = []
skew_sum_list = []
kurt_sum_list = []
shrinkage_list = []
peak_factor_list = []  # 存储Peak factor特征
waveform_factor_list = []  # 存储Waveform factor特征
impulse_factor_list = []  # 存储Impulse factor特征
mean_square_frequency_list = []  # 存储Mean square frequency特征
gravity_frequency_list = []  # 存储Gravity frequency特征
variance_frequency_list = []  # 存储Variance frequency特征

# 绘制曲线图并提取特征
fig, ax = plt.subplots()

for i in range(len(data)):
    x = data.columns
    y = data.iloc[i, :]

    # 过滤为0的数据点
    non_zero_indices = y.to_numpy().nonzero()[0]
    y = y.iloc[non_zero_indices]
    x = x[non_zero_indices]

    # 如果y中没有数据，则跳过当前曲线
    if len(y) == 0:
        continue

    # 计算标准差特征
    std = y.std()

    # 计算均值特征
    mean = y.mean()

    # 计算偏度特征
    skew = ((y - mean) / std) ** 3
    skew_sum = skew.sum()

    # 计算峰度特征
    kurt = ((y - mean) / std) ** 4
    kurt_sum = kurt.sum()

    # 计算收缩力估计特征：对数平均值
    shrinkage = np.exp(np.sum(np.log(y)) / len(y))

    # 计算Peak factor特征
    max_value = y.max()
    peak_factor = max_value / mean

    # 计算Waveform factor特征
    abs_y = np.abs(y)
    max_abs_value = abs_y.max()
    rms = np.sqrt(np.mean(y ** 2))
    waveform_factor = max_abs_value / rms

    # 计算Impulse factor特征
    impulse_factor = max_abs_value / np.sqrt(np.sum(y ** 2))

    # 计算Mean square frequency特征
    f, Pxx = welch(y)
    mean_square_frequency = np.sqrt(np.sum(f * Pxx) / np.sum(Pxx))

    # 计算Gravity frequency特征
    gravity_frequency = np.sum(f * Pxx) / np.sum(Pxx)

    # 计算Variance frequency特征
    variance_frequency = np.sqrt(np.sum((f - gravity_frequency) ** 2 * Pxx) / np.sum(Pxx))

    # 绘制曲线图
    ax.plot(x, y)

    # 存储特征值
    std_list.append(std)
    skew_sum_list.append(skew_sum)
    kurt_sum_list.append(kurt_sum)
    shrinkage_list.append(shrinkage)
    peak_factor_list.append(peak_factor)
    waveform_factor_list.append(waveform_factor)
    impulse_factor_list.append(impulse_factor)
    mean_square_frequency_list.append(mean_square_frequency)
    gravity_frequency_list.append(gravity_frequency)
    variance_frequency_list.append(variance_frequency)

# 更新DataFrame的定义
features_df = pd.DataFrame({
    'Standard Deviation': std_list,
    'Skewness Sum': skew_sum_list,
    'Kurtosis Sum': kurt_sum_list,
    'Shrinkage': shrinkage_list,
    'Peak Factor': peak_factor_list,
    'Waveform Factor': waveform_factor_list,
    'Impulse Factor': impulse_factor_list,
    'Mean Square Frequency': mean_square_frequency_list,
    'Gravity Frequency': gravity_frequency_list,     #没用到
    'Variance Frequency': variance_frequency_list    #没用到
}, index=labels)

# 将特征DataFrame保存到Excel文件中
features_df.to_excel(r'C:\新建文件夹\DATA\train\ma4.xlsx')

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def predict(model_file, data_file):
    # 加载保存的最佳模型
    loaded_model = joblib.load(model_file)

    # 加载要预测的数据
    data = pd.read_excel(data_file)

    # 分割特征值和标签
    X = data.iloc[:, 1:].values
    y_true = data['line_number'].values

    # 使用加载的模型进行预测
    y_pred = loaded_model.predict(X)

    # 计算混淆矩阵
    cm = confusion_matrix(y_true, y_pred)

    # 可视化混淆矩阵
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

    # 将预测结果转换为DataFrame对象
    result_df = pd.DataFrame({'Predicted': y_pred})

    # 将DataFrame保存为Excel文件
    result_df.to_excel(r'D:\BaiduNetdiskDownload\luolie\6\999.xlsx', index=False)

    # 返回预测结果的Series对象
    return pd.Series(y_pred)

# 定义保存最佳模型的文件路径和包含要预测的数据的文件路径
model_file = 'best_model.pkl'
data_file = r'D:\BaiduNetdiskDownload\luolie\6\9.xlsx'

# 调用predict函数并打印预测结果
y_new_pred = predict(model_file, data_file)
print('新数据的预测结果:')
print(y_new_pred)
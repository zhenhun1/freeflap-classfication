import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import joblib

# 加载训练集数据
train_data = pd.read_excel(r'12.27/features2.xlsx')

# 分割特征值和标签
X_train = train_data.iloc[:, 1:].values
y_train = train_data.iloc[:, 0].astype(str).values

# 初始化变量来保存最佳模型和性能
best_accuracy = 0
best_model = None
best_precision = 0
best_recall = 0
best_f1 = 0

# 进行100轮训练
for i in range(50):
    # 创建随机森林分类器
    random_forest = RandomForestClassifier()

    # 训练分类器
    random_forest.fit(X_train, y_train)

    # 加载验证集数据
    val_data = pd.read_excel(r'12.27/valfeatures1.xlsx')

    # 分割特征值和标签
    X_val = val_data.iloc[:, 1:].values
    y_val = val_data.iloc[:, 0].astype(str).values

    # 在训练集上进行预测
    y_train_pred = random_forest.predict(X_train)

    # 在验证集上进行预测
    y_val_pred = random_forest.predict(X_val)

    # 计算训练集和验证集准确率、精确率、召回率和F1值
    train_acc = accuracy_score(y_train, y_train_pred)
    val_acc = accuracy_score(y_val, y_val_pred)
    precision = precision_score(y_val, y_val_pred, pos_label='bad')
    recall = recall_score(y_val, y_val_pred, pos_label='bad')
    f1 = f1_score(y_val, y_val_pred, pos_label='bad')

    # 打印训练集和验证集的指标
    print(f"第{i+1}轮训练 - Train Acc: {train_acc:.4f}, Val Acc: {val_acc:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")

    # 更新最佳模型和指标
    if val_acc > best_accuracy:
        best_accuracy = val_acc
        best_model = random_forest
    if precision > best_precision:
        best_precision = precision
    if recall > best_recall:
        best_recall = recall
    if f1 > best_f1:
        best_f1 = f1

# 保存最佳模型
joblib.dump(best_model, 'best_model.pkl')

# 打印最佳模型性能
print('最佳模型性能:')
print(f"Accuracy: {best_accuracy:.4f}, Precision: {best_precision:.4f}, Recall: {best_recall:.4f}, F1: {best_f1:.4f}")

# 在测试集上进行预测
test_data = pd.read_excel('12.27/test.xlsx')
X_test = test_data.iloc[:, 1:].values
y_test = test_data.iloc[:, 0].astype(str).values
y_test_pred = best_model.predict(X_test)

# 显示混淆矩阵
confusion_mat = confusion_matrix(y_test, y_test_pred)
print('混淆矩阵:')
print(confusion_mat)

# 加载模型
loaded_model = joblib.load('1230best_model.pkl')

# 使用加载的模型进行预测
new_data = pd.read_excel('12.27/test.xlsx')
X_new = new_data.iloc[:, 1:].values
y_new_pred = loaded_model.predict(X_new)

# 打印新数据的预测结果
print('新数据的预测结果:')
print(y_new_pred)

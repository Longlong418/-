import pandas as pd
from sklearn.model_selection import train_test_split
# 加载CSV文件
data = pd.read_csv('diabetes.csv')
# 假设CSV文件包含特征列和目标列
X = data.drop('Outcome', axis=1)  # 特征列
y = data['Outcome']  # 目标列
# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# 将训练集保存到新的CSV文件
train_data = pd.concat([X_train, y_train], axis=1)
train_data.to_csv('data/diabetes_train_data.csv', index=False)
# 将测试集保存到新的CSV文件
test_data = pd.concat([X_test, y_test], axis=1)
test_data.to_csv('data/diabetes_test_data.csv', index=False)
# import pandas as pd

# print(list(pd.read_csv('NBA.csv').columns)[:-1])

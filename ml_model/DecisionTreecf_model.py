from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, auc, precision_recall_curve
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler, label_binarize
from utils.draw_pic import draw_ROC
from utils.draw_pic import draw_pre_rec
from utils.draw_pic import draw_learning_curve
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import string
import random
import pickle

warnings.filterwarnings("ignore")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 生成指定长度的随字符串


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


random_string = generate_random_string(5)

# def draw_ROC(y_score, y_test):
#     y_test_binary = label_binarize(y_test, classes=[0, 1, 2])
#     fpr, tpr, thresholds = roc_curve(y_test_binary[:, 1], y_score)
#     roc_auc = auc(fpr, tpr)
#     plt.figure()
#     plt.plot(fpr, tpr, color='darkorange', lw=2,
#              label='ROC curve (AUC = %0.2f)' % roc_auc)
#     plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
#     plt.xlabel('False Positive Rate')
#     plt.ylabel('True Positive Rate')
#     plt.title('ROC曲线')
#     plt.legend(loc="lower right")
#     plt.show()


# def draw_pre_rec(precision, recall):
#     plt.figure()
#     plt.step(recall, precision, color='b', alpha=0.2, where='post')
#     plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
#     plt.xlabel('Recall')
#     plt.ylabel('Precision')
#     plt.ylim([0.0, 1.05])
#     plt.xlim([0.0, 1.0])
#     plt.title('Precision-Recall curve(精确率-召回率曲线)')
#     plt.show()


# def draw_learning_curve(estimator, X, y):
#     train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=5,
#                                                             train_sizes=np.linspace(
#                                                                 0.1, 1.0, 10),
#                                                             scoring='accuracy')
#     train_mean = np.mean(train_scores, axis=1)
#     train_std = np.std(train_scores, axis=1)
#     test_mean = np.mean(test_scores, axis=1)
#     test_std = np.std(test_scores, axis=1)

#     plt.figure()
#     plt.plot(train_sizes, train_mean, 'o-',
#              color="r", label="Training Accuracy")
#     plt.plot(train_sizes, test_mean, 'o-', color="g",
#              label="Cross-validation Accuracy")
#     plt.fill_between(train_sizes, train_mean - train_std,
#                      train_mean + train_std, alpha=0.2, color="r")
#     plt.fill_between(train_sizes, test_mean - test_std,
#                      test_mean + test_std, alpha=0.2, color="g")
#     plt.xlabel("Training Examples")
#     plt.ylabel("Accuracy")
#     plt.legend(loc="best")
#     plt.title("Learning Curve(学习曲线)")
#     plt.show()


class decision_tree_model():
    def __init__(self):
        self.params = {'criterion': 'gini',
                       'max_depth': None, 'min_samples_split': 2}
        self.train_file = "data/cancer_train.xlsx"
        self.test_file = "data/cancer_test.xlsx"
        self.name = "决策树分类器"
        self.exp = {}  # 实验结果字典形式
        self.exp_pic = {}  # 实验结果图片路径字典形式
        self.model_path = ""
        self.headers = []  # 数据集的表头

    def start_train(self):
        self.data_process()
        self.train_model()
        self.model_eval()
        # 将训好的模型保存下来
        model_path = "Trained_model\\"+random_string+self.name+"model.pkl"

        with open(model_path, 'wb') as file:
            pickle.dump(self.model, file)
        self.model_path = model_path

    def data_process(self):
        if self.train_file[-4:] == "xlsx" or self.train_file[-3:] == "xls":
            data = np.array(pd.read_excel(self.train_file, header=0))
            test = np.array(pd.read_excel(self.test_file, header=0))
            self.headers = list(pd.read_excel(self.train_file).columns)[:-1]
        else:
            data = np.array(pd.read_csv(self.train_file, header=0))
            test = np.array(pd.read_csv(self.test_file, header=0))
            self.headers = list(pd.read_csv(self.train_file).columns)[:-1]
        # print(data.shape)
        self.x_train = data[:, :-1]
        self.y_train = data[:, -1]
        self.x_test = test[:, :-1]
        self.y_test = test[:, -1]
        # 获取维度和数量
        self.train_sum = data.shape[0]-1
        self.train_dim = data.shape[1]-1
        self.test_sum = test.shape[0]-1
        self.test_dim = test.shape[1]-1

    def train_model(self):
        self.model = DecisionTreeClassifier(**self.params)
        self.model.fit(self.x_train, self.y_train)

    def model_eval(self):
        y_pred = self.model.predict(self.x_test)
        self.acc = accuracy_score(self.y_test, y_pred)
        self.precision = precision_score(self.y_test, y_pred, average=None)
        self.re_score = recall_score(self.y_test, y_pred, average=None)
        self.F1_score = f1_score(self.y_test, y_pred, average="micro")
        self.exp['acc'] = str(self.acc)
        self.exp['precision'] = str(self.precision)
        self.exp['re_score'] = str(self.re_score)
        self.exp['F1_score'] = str(self.F1_score)
        # ROC curve
        y_score = self.model.predict_proba(self.x_test)
        if y_score.ndim != 1:
            y_score = y_score[:, 1]
        self.roc_path = draw_ROC(y_score, self.y_test)

        # Precision-Recall curve
        y_test_binary = label_binarize(self.y_test, classes=[0, 1, 2])
        precision, recall, thresholds = precision_recall_curve(
            y_test_binary[:, 1], y_pred)
        self.pr_path = draw_pre_rec(precision, recall)

        # Learning curve
        self.learn_path = draw_learning_curve(
            self.model, self.x_train, self.y_train)
        # 图片路径字典形式
        self.exp_pic['roc_path'] = self.roc_path
        self.exp_pic['pr_path'] = self.pr_path
        self.exp_pic['learn_path'] = self.learn_path


# dt = decision_tree_model()
# dt.start_train()
# print(dt.acc)

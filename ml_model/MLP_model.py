from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, precision_recall_curve, auc
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import label_binarize
from sklearn.preprocessing import StandardScaler
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
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


random_string = generate_random_string(5)


class MLPClassifier_model():
    def __init__(self):
        self.params = {'batch_size': 200, 'activation': 'relu',
                       'max_iter': 200, 'learning_rate_init': 0.001}
        self.train_file = "data/iris_train.xlsx"
        self.test_file = "data/iris_test.xlsx"
        self.name = "MLPClassifier"
        self.exp = {}  # 实验结果字典形式
        self.exp_pic = {}  # 实验结果图片路径字典形式
        self.model_path = ""  # 模型路径
        self.headers = []

    def start_train(self):
        self.data_process()
        self.train_model()
        self.model_eval()
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
        self.model = MLPClassifier(**self.params)
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

        # 绘制ROC曲线

        y_score = self.model.predict_proba(self.x_test)
        print(y_score.ndim)
        if y_score.ndim != 1:
            y_score = y_score[:, 1]

        self.roc_path = draw_ROC(y_score, self.y_test)
        # 绘制精确率-召回率曲线
        y_test_binary = label_binarize(self.y_test, classes=[0, 1, 2])
        precision, recall, thresholds = precision_recall_curve(
            y_test_binary[:, 1], y_score)
        self.pr_path = draw_pre_rec(precision, recall)
        # 绘制学习曲线
        self.learn_path = draw_learning_curve(
            self.model, self.x_train, self.y_train)
        # 图片路径字典形式
        self.exp_pic['roc_path'] = self.roc_path
        self.exp_pic['pr_path'] = self.pr_path
        self.exp_pic['learn_path'] = self.learn_path


# l = MLPClassifier_model()
# l.start_train()
# print(l.acc)

# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, auc, precision_recall_curve
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler, label_binarize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import random
import string

warnings.filterwarnings("ignore")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# 生成指定长度的随字符串
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


random_string = generate_random_string(5)


def draw_ROC(y_score, y_test):
    y_test_binary = label_binarize(y_test, classes=[0, 1, 2])
    fpr, tpr, thresholds = roc_curve(y_test_binary[:, 1], y_score)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2,
             label='ROC curve (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC曲线')
    plt.legend(loc="lower right")
    plt.savefig("exp_pic\ROC曲线"+random_string+".png")
    return "exp_pic\ROC曲线"+random_string+".png"


def draw_pre_rec(precision, recall):
    plt.figure()
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall curve(P-R曲线)')
    plt.savefig("exp_pic\PR曲线"+random_string+".png")
    return "exp_pic\PR曲线"+random_string+".png"


def draw_learning_curve(estimator, X, y):
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=5,
                                                            train_sizes=np.linspace(
                                                                0.1, 1.0, 10),
                                                            scoring='accuracy')
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.plot(train_sizes, train_mean, 'o-',
             color="r", label="Training Accuracy")
    plt.plot(train_sizes, test_mean, 'o-', color="g",
             label="Cross-validation Accuracy")
    plt.fill_between(train_sizes, train_mean - train_std,
                     train_mean + train_std, alpha=0.2, color="r")
    plt.fill_between(train_sizes, test_mean - test_std,
                     test_mean + test_std, alpha=0.2, color="g")
    plt.xlabel("Training Examples")
    plt.ylabel("Accuracy")
    plt.legend(loc="best")
    plt.title("Learning Curve(学习曲线)")
    plt.savefig("exp_pic\学习曲线"+random_string+".png")
    return "exp_pic\学习曲线"+random_string+".png"

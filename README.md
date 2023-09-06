## （一）项目功能介绍
### (a)总体介绍：

本项目包含两个界面：用户界面和管理员界面，用户界面包含三个模块：模型训练模块、个人实验记录管理、个人信息模块，模型训练模块包含上传测试集训练集、选择模型、参数选择、训练模型的功能，个人信息模块提供修改个人信息以及密码的功能，个人实验记录管理有查看实验结果、模型预测、查看数据集和删除对应实验记录的功能，管理员界面包含用户信息管理模块、所有用户的实验记录管理模块、此外本项目设置超级管理员和普通管理员两个等级，超级管理员可以在管理员信息管理页面对普通管理员信息进行增删改查，超级管理员和普通管理员可以对用户信息进行增删改查，同时可以管理所有用户的实验记录，功能和普通用户大差不差。以下是程序流程图
![程序流程图](https://img.xlonglong.cn/img/程序流程图.png)

### (b):整体架构：

首先通过main.py文件进入login包下的main_login.py模块，进行登录，main_login.py下有三个界面，用户登录、用户注册、管理员登录。分别对应user_login.py、signup.py、admin_login.py模块，用户登录模块登录成功后，跳转到user包下的user_main.py模块，该模块有模型训练、个人信息管理、实验记录管理，分别对应train.py、user_information.py 模块以及exp包下的record.py模块。训练需要引入ml_model包下的三个对应模块，训练结束后，展示的结果为user包下的result.py模块。在实验记录管理模块，通过他提供实验结果展示、模型预测、数据集查看分别对应exp包下的resul2.py模块、predict.py、data_info.py模块，在管理员登录成功后，跳转到admin包下的admin_main.py模块，该模块有用户管理、管理员管理、实验记录管理，分别对应该目录下的user_mgt.py、admin_mgt.py、record_mgt.py模块

## （二）选用的数据集
威斯康星州乳腺癌数据集
鸢尾花数据集
葡萄酒数据集
NBA球员是否为全明星数据集
心脏病数据集
糖尿病数据集
来源：Kaggle: [Your Machine Learning and Data Science Community](https://www.kaggle.com/)
[API 参考-scikit-learn中文社区](https://scikit-learn.org.cn/lists/3.html#sklearn.datasets%EF%BC%9A%E6%95%B0%E6%8D%AE%E9%9B%86)

## （三）使用的机器学习算法
### (a)模型采用:
模型采取了线性逻辑回归、支持向量机、决策树、多层感知机
### (b)第三方库选取
sklearn.linear_model.LogisticRegression
sklearn.svm.LinearSVC 
sklearn.tree.DecisionTreeClassifier
sklearn.neural_network.MLPClassifier
### (c)超参设置：
LogisticRegression:  penalty、C、max_iter、solver
LinearSVC      :  penalty、C、tol、loss
DecisionTreeClassifier: criterion、max_depth、min_samples_split、max_features
MLPClassifier   :batch_size、max_iter、activation(激活函数)、learning_rate_init(学习率)

## （四）数据库设计

### （一）实体关系设计

实体关系包含用户、测试集、训练集、实验记录、模型。首先用户可以通过用户名注册，该关系会记录在用户数据库中，也可以通过管理员添加用户，模型选择由用户选择与上传，用户点击训练模型之后，会将测试集以及训练集的路径以及他的信息存在测试集以及训练集中，训练出来的实验结果会存在实验记录中，该模型也会保存下来，，该模型包含了这次实验的参数、X特征值以及保存的路径，会存在模型实体关系中，由于一条实验记录对应一个模型，所以模型和实验记录是一对一的关系，而一个测试集和训练集可以对应多条实验记录，所以他与实验记录是一对多的关系，ER图如图所示
![20230906111305](https://img.xlonglong.cn/img/20230906111305.png)

### （二）数据库的实现
users(用户)表：uname(varchar，主键,用户名)、email(varchar，邮箱)、passwords(varchar,密码)、entime(date，注册时间)、is_admin(INT,是否为管理员，0为用户，1为普通管理员，2为超级管理员)。

**表1.1 users(用户)表**
| 字段名      | 类型      | 长度 | 备注          | 说明          |
|-------------|-----------|------|---------------|---------------|
| uname       | varchar   | 255  | Primary key   | 用户名        |
| email       | varchar   | 255  | Not null      | 邮箱          |
| passwords   | varchar   | 255  | Not null      | 密码          |
| entime      | varchar   | 255  | Not null      | 注册时间      |
| is_admin    | Int       | 11   | Not null      | 是否管理员    |

model(模型)表：m_id(int，主键,模型id)、mname(varchar，模型名字)、mparm(varchar,模型参数)、model_path(varchar，模型路径)、x(text,特征值)。

**表1.2model(模型)表**
| 字段名         | 类型      | 长度   | 备注          | 说明          |
|----------------|-----------|--------|---------------|---------------|
| m_id           | Int       | 11     | Primary key   | 模型id        |
| mname          | varchar   | 255    | Not null      | 模型名字      |
| mparm          | Text      | 65535  | Not null      | 模型参数      |
| model_path     | varchar   | 255    | Not null      | 模型路径      |
| x              | text      | 65535  | Not null      | 特征值        |

test(测试集)表：test_id(int，主键,测试集id)、test_path(varchar，测试集路径)、test_sum(varchar,样本总数)、test_dim(varchar，测试集维度)、users_uname(varchar，用户名(外键，from users表，表示由谁上传)。

**表1.3test(测试集)表**
| 字段名         | 类型      | 长度   | 备注          | 说明          |
|----------------|-----------|--------|---------------|---------------|
| test_id        | Int       | 11     | Primary key   | 测试集id      |
| test_path      | varchar   | 255    | Not null      | 测试集路径    |
| test_sum       | varchar   | 255    | Not null      | 样本总数      |
| test_dim       | varchar   | 255    | Not null      | 测试集维度    |
| users_uname    | Varchar   | 255    | Not null      | 用户名        |


train(训练集)表：t_id(int，主键,训练集id)、train_path(varchar，训练集路径)、train_sum(varchar,样本总数)、train_dim(varchar，训练集维度)、users_uname(varchar，用户名(外键，from users表，表示由谁上传)。
**表1.4train(训练集)表**
| 字段名         | 类型      | 长度   | 备注          | 说明          |
|----------------|-----------|--------|---------------|---------------|
| t_id           | Int       | 11     | Primary key   | 训练集id      |
| train_path     | varchar   | 255    | Not null      | 训练集路径    |
| train_sum      | varchar   | 255    | Not null      | 样本总数      |
| train_dim      | varchar   | 255    | Not null      | 训练集维度    |
| users_uname    | Varchar   | 255    | Not null      | 用户名        |




record(实验记录)表：r_id(int，主键,实验id)、result(varchar，实验结果)、record_date(datetime,实验时间)、pic_path(varchar,实验结果图的路径)、users_uname(varchar，用户名外键，from users表,表示该实验是谁做的)、test_test_id(int，测试集id(外键，from test表，表示该实验所用的测试集)，train_t_id(int,训练集id(外键，from train表，表示该实验所用的训练集)，model_m_id(int,id，外键，from model表，表示该实验训练出来的模型)。
**表1.5record(实验记录)表**
| 字段名         | 类型      | 长度     | 备注          | 说明          |
|----------------|-----------|----------|---------------|---------------|
| r_id           | Int       | 11       | Primary key   | 实验id        |
| result         | varchar   | 255      | Not null      | 实验结果      |
| record_date    | datetime  | 255      | Not null      | 实验时间      |
| pic_path       | varchar   | 255      | Not null      | 实验结果图的路径 |
| users_uname    | Varchar   | 255      | Not null      | 用户名        |
| test_test_id   | int       | 11       | Not null      | 测试集id      |
| train_t_id     | int       | 11       | Not null      | 训练集id      |
| model_m_id     | int       | 11       | Not null      | 模型id        |


## （五）部分功能模块展示
![20230906112131](https://img.xlonglong.cn/img/20230906112131.png)

![20230906112148](https://img.xlonglong.cn/img/20230906112148.png)


![20230906112221](https://img.xlonglong.cn/img/20230906112221.png)

![20230906112250](https://img.xlonglong.cn/img/20230906112250.png)

![20230906112339](https://img.xlonglong.cn/img/20230906112339.png)

![20230906112422](https://img.xlonglong.cn/img/20230906112422.png)

## 补充

环境：windows 10 x64 
数据库：MySQL8.0:https://www.mysql.com/cn/
用到的第三方模块：PySide6、sklearn、matplotlib、pandas、numpy、mysql.connector
开发工具：vs-code 1.70.1 
完成日期：2023年7月

这是大二下的一个课设，这次课设学到了很多东西，但是学到最重要的东西是：保护好自己的知识产权。被剽窃的滋味是真不好受。。甚至那个人都不和你打声招呼的时候。但凡打声招呼我也很乐意分享的。


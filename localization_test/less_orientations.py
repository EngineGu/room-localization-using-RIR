from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import config.dataset_setting
import util.file_io
import util.dataset

train_dataset_condition = 8
test_dataset_condition = 8
# DATASET_CONDITION = [
#     "exp20210114_HW_Quiet_Strong_Unchanged_orientation_4_sample_40", # condition 0
#     "exp20210716_OP_Noisy_Strong_Unchanged_orientation_4_sample_40", # condition 1
#     "exp20210716_OP_Quiet_Strong_Unchanged_orientation_4_sample_40", # condition 2
#     "exp20210716_OP_Quiet_Weak_Unchanged_orientation_4_sample_40",   # condition 3
#     "exp20220330_HW_Quiet_Strong_Changed_orientation_4_sample_40",   # condition 4
#     "exp20220330_HW_Quiet_Strong_Unchanged_orientation_4_sample_40", # condition 5
#     "exp20220330_HW_Quiet_Strong_Unchanged_orientation_2_sample_20", # condition 6
#     "exp20220330_HW_Quiet_Strong_Unchanged_orientation_4_sample_20", # condition 7
#     "exp20220330_HW_Quiet_Strong_Unchanged_orientation_2_sample_40", # condition 8
#     "exp20220330_HW_Noisy_Strong_Unchanged_orientation_4_sample_40", # condition 9
# ]
# 一、room_level
localization_level = "room_level" # room_level,location_level
print("一、" + localization_level+":\n")
## （一）leave_samples
leave_type = "leave_samples" # leave_samples,leave_1_orientation,leave_1_location
print("（一）" + leave_type + ":\n")
### 1、获取数据集
train_data,train_label,_,_ = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[train_dataset_condition],
    leave_type,localization_level)

_,_,test_data,test_label = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[test_dataset_condition],
    leave_type,localization_level)
# 2、利用数据集训练SVM并预测
classifier=svm.SVC(C=2,kernel='linear',gamma=10,decision_function_shape='ovo') # ovr:一对多策略
classifier.fit(train_data,train_label.ravel()) #ravel函数在降维时默认是行序优先
test_label_from_model=classifier.predict(test_data) #预测测试集的房间号
# 3、输出预测准确率和错误的值
print("测试集的预测准确度：", accuracy_score(test_label,test_label_from_model))
# print("测试集中预测错误的数据：")
# for i in range(0,test_label.size):
#     if test_label[i] != test_label_from_model[i]:
#         print("真实值:",util.dataset.get_inf_from_label(test_label[i]),
#             ";预测值:",util.dataset.get_inf_from_label(test_label_from_model[i])
#             )
## （二）leave_1_orientation
leave_type = "leave_1_orientation" # leave_samples,leave_1_orientation,leave_1_location
print("（二）" + leave_type + ":\n")
### 1、获取数据集
train_data,train_label,_,_ = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[train_dataset_condition],
    leave_type,localization_level)

_,_,test_data,test_label = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[test_dataset_condition],
    leave_type,localization_level)
# 2、利用数据集训练SVM并预测
classifier=svm.SVC(C=2,kernel='linear',gamma=10,decision_function_shape='ovo') # ovr:一对多策略
classifier.fit(train_data,train_label.ravel()) #ravel函数在降维时默认是行序优先
test_label_from_model=classifier.predict(test_data) #预测测试集的房间号
# 3、输出预测准确率和错误的值
print("测试集的预测准确度：", accuracy_score(test_label,test_label_from_model))
# print("测试集中预测错误的数据：")
# for i in range(0,test_label.size):
#     if test_label[i] != test_label_from_model[i]:
#         print("真实值:",util.dataset.get_inf_from_label(test_label[i]),
#             ";预测值:",util.dataset.get_inf_from_label(test_label_from_model[i])
#             )
## leave_1_location
leave_type = "leave_1_location" # leave_samples,leave_1_orientation,leave_1_location
print("（三）" + leave_type + ":\n")
### 1、获取数据集
train_data,train_label,_,_ = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[train_dataset_condition],
    leave_type,localization_level)

_,_,test_data,test_label = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[test_dataset_condition],
    leave_type,localization_level)
# 2、利用数据集训练SVM并预测
classifier=svm.SVC(C=2,kernel='linear',gamma=10,decision_function_shape='ovo') # ovr:一对多策略
classifier.fit(train_data,train_label.ravel()) #ravel函数在降维时默认是行序优先
test_label_from_model=classifier.predict(test_data) #预测测试集的房间号
# 3、输出预测准确率和错误的值
print("测试集的预测准确度：", accuracy_score(test_label,test_label_from_model))
# print("测试集中预测错误的数据：")
# for i in range(0,test_label.size):
#     if test_label[i] != test_label_from_model[i]:
#         print("真实值:",util.dataset.get_inf_from_label(test_label[i]),
#             ";预测值:",util.dataset.get_inf_from_label(test_label_from_model[i])
#             )

# 二、location_level
localization_level = "location_level" # room_level,location_level
print("二、" + localization_level+":\n")
## （一）leave_samples
leave_type = "leave_samples" # leave_samples,leave_1_orientation,leave_1_location
print("（一）" + leave_type + ":\n")
### 1、获取数据集
train_data,train_label,_,_ = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[train_dataset_condition],
    leave_type,localization_level)

_,_,test_data,test_label = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[test_dataset_condition],
    leave_type,localization_level)
# 2、利用数据集训练SVM并预测
classifier=svm.SVC(C=2,kernel='linear',gamma=10,decision_function_shape='ovo') # ovr:一对多策略
classifier.fit(train_data,train_label.ravel()) #ravel函数在降维时默认是行序优先
test_label_from_model=classifier.predict(test_data) #预测测试集的房间号
# 3、输出预测准确率和错误的值
print("测试集的预测准确度：", accuracy_score(test_label,test_label_from_model))
# print("测试集中预测错误的数据：")
# for i in range(0,test_label.size):
#     if test_label[i] != test_label_from_model[i]:
#         print("真实值:",util.dataset.get_inf_from_label(test_label[i]),
#             ";预测值:",util.dataset.get_inf_from_label(test_label_from_model[i])
#             )
## （二）leave_1_orientation
leave_type = "leave_1_orientation" # leave_samples,leave_1_orientation,leave_1_location
print("（二）" + leave_type + ":\n")
### 1、获取数据集
train_data,train_label,_,_ = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[train_dataset_condition],
    leave_type,localization_level)

_,_,test_data,test_label = util.file_io.load_txt_files_in_dataset_conditions(
    config.file_io.DATASET_PARENT_PATH,
    config.dataset_setting.DATASET_CONDITION[test_dataset_condition],
    leave_type,localization_level)
# 2、利用数据集训练SVM并预测
classifier=svm.SVC(C=2,kernel='linear',gamma=10,decision_function_shape='ovo') # ovr:一对多策略
classifier.fit(train_data,train_label.ravel()) #ravel函数在降维时默认是行序优先
test_label_from_model=classifier.predict(test_data) #预测测试集的房间号
# 3、输出预测准确率和错误的值
print("测试集的预测准确度：", accuracy_score(test_label,test_label_from_model))
# print("测试集中预测错误的数据：")
# for i in range(0,test_label.size):
#     if test_label[i] != test_label_from_model[i]:
#         print("真实值:",util.dataset.get_inf_from_label(test_label[i]),
#             ";预测值:",util.dataset.get_inf_from_label(test_label_from_model[i])
#             )

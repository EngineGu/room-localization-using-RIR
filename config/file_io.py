import os
import librosa
import config.exp_setting
import config.dataset_setting

# 文件系统的参数
## 一、数据文件所在的父目录
DATA_FOLDER_PARENT_PATH = os.path.abspath("..\\data") + "\\"

## 二、MLS信号音频相关
### 1、MLS信号音频的路径
MLS_SIGNAL_PATH = DATA_FOLDER_PARENT_PATH + "mls_signal\\mls_signal_1_time.wav" # MLS音频的路径
MLS_SIGNAL,_ = librosa.load(MLS_SIGNAL_PATH, sr = config.exp_setting.SAMPLE_RATE)

## 三、人声噪音音频相关
### 1、人声噪音音频的路径
BABBLE_NOISE_PATH = DATA_FOLDER_PARENT_PATH + "noise\\babble.wav"
BABBLE_NOISE,_ = librosa.load(BABBLE_NOISE_PATH,sr = config.exp_setting.SAMPLE_RATE)

## 四、文件名的组成部分
MLS_RECORD_FILENAME_PART_Room = "Room_"
MLS_RECORD_FILENAME_PART_Corridor = "Corridor_"
MLS_RECORD_FILENAME_PART_Location = "_Location_"
MLS_RECORD_FILENAME_PART_Orientation = "_Orientation_"
MLS_RECORD_FILENAME_PART_Sample = "_Sample_"
MLS_RECORD_FILENAME_PART_Extension_WAV = ".wav"
MLS_RECORD_FILENAME_PART_Extension_PKL = ".pkl"

## 五、MLS录音音频相关
### 1、MLS录音音频(取向粒度)所在的目录
MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH = DATA_FOLDER_PARENT_PATH + "mls_record_in_orientations\\"
MLS_RECORD_IN_ORIENTATIONS_PATH_IN_EXP_CONDITION = [
    MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH + config.exp_setting.EXP_CONDITION[0] +"\\",
    MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH + config.exp_setting.EXP_CONDITION[1] +"\\",
    MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH + config.exp_setting.EXP_CONDITION[2] +"\\",
    MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH + config.exp_setting.EXP_CONDITION[3] +"\\",
    MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH + config.exp_setting.EXP_CONDITION[4] +"\\",
    MLS_RECORD_IN_ORIENTATIONS_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\",
]
### 2、MLS录音音频(采样粒度)所在的目录
MLS_RECORD_IN_SAMPLES_PARENT_PATH = DATA_FOLDER_PARENT_PATH + "mls_record_in_samples\\"
MLS_RECORD_IN_SAMPLES_PATH_IN_EXP_CONDITION = [
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[0] +"\\",
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[1] +"\\",
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[2] +"\\",
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[3] +"\\",
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[4] +"\\",
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\",
    MLS_RECORD_IN_SAMPLES_PARENT_PATH + config.exp_setting.EXP_CONDITION[6] +"\\"
]

## 六、MLS录音音频（采样粒度）的RIR所在的目录
REAL_RIR_PARENT_PATH = DATA_FOLDER_PARENT_PATH + "rir_of_mls_record_in_samples\\"
REAL_RIR_PATH_IN_EXP_CONDITION = [
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[0] +"\\",
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[1] +"\\",
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[2] +"\\",
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[3] +"\\",
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[4] +"\\",
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\",
    REAL_RIR_PARENT_PATH + config.exp_setting.EXP_CONDITION[6] +"\\",
]

## 七、MLS录音音频（采样粒度）的RIR的MFCC所在的目录
MFCC_PARENT_PATH = DATA_FOLDER_PARENT_PATH + "mfcc_of_rir_of_mls_record_in_samples\\"
MFCC_PATH_IN_EXP_CONDITION = [
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[0] +"\\",
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[1] +"\\",
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[2] +"\\",
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[3] +"\\",
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[4] +"\\",
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\",
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[6] +"\\",
]

## 八、数据集条件下MFCC所在的目录
MFCC_PARENT_PATH = DATA_FOLDER_PARENT_PATH + "mfcc_of_rir_of_mls_record_in_samples\\"
MFCC_PATH_IN_DATASET_CONDITION = [
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[0] +"\\", # condition 0
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[1] +"\\", # condition 1
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[2] +"\\", # condition 2
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[3] +"\\", # condition 3
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[4] +"\\", # condition 4
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\", # condition 5
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\", # condition 6
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\", # condition 7
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[5] +"\\", # condition 8
    MFCC_PARENT_PATH + config.exp_setting.EXP_CONDITION[6] +"\\", # condition 9
]

## 八、数据集文件所在的目录
DATASET_PARENT_PATH = DATA_FOLDER_PARENT_PATH + "dataset_of_mfcc_of_rir_of_mls_record_in_samples\\"
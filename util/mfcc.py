import librosa
import numpy as np

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import config.dataset_setting

# 定义计算房间冲激响应的梅尔倒频谱的函数
def get_mfcc_of_sample_rir(rir):
    """计算输入的房间的房间冲激响应的特征——梅尔倒频谱

    将某个房间中某个位置某个取向某次采样的录音片段的房间冲激响应的梅尔倒频谱算出来

    Args:
        mls_audio：mls音频
        recording_audio：某个房间中某个位置某个取向某次采样的录音片段。
        
    Return：
        某个房间中某个位置某个取向某次采样的rir的mfcc
    """
    # 求rir的mfcc:调用librosa库的mfcc函数计算
    mfcc = librosa.feature.mfcc(y=rir,sr=config.exp_setting.SAMPLE_RATE,
        n_mfcc=config.dataset_setting.MFCC_EIGENVALUE_AMOUNT)
    return mfcc


def align_mfcc(original_mfcc):
    "将各房间的mfcc数组对齐成同shape的函数"
    data_frame_amount_of_original_mfcc =  original_mfcc.shape[1] # 输入数组的实际数据帧数量
    complement_data_frame_amount = config.dataset_setting.MFCC_DATAFRAME_AMOUNT - data_frame_amount_of_original_mfcc # 对齐要补的数据帧数量等于最大的数据帧数量 - 实际数据帧数量
    # 构造用于对齐要补的数据帧数组
    zeros_list_for_complement_data_frames = []
    for i in range(0,complement_data_frame_amount):
        zeros_list_for_complement_data_frames.append(0)
    # 进行补齐
    aligned_mfcc = np.empty([config.dataset_setting.MFCC_EIGENVALUE_AMOUNT,config.dataset_setting.MFCC_DATAFRAME_AMOUNT], dtype = float, order = 'C')
    for i in range(0,len(original_mfcc)):
        aligned_mfcc[i] = np.append(original_mfcc[i], zeros_list_for_complement_data_frames) # 对每一mfcc特征值，补进去若干数据帧
    return aligned_mfcc


def flatten_mfcc(aligned_mfcc):
    '''展平mfcc:定义将各房间的mfcc数组从(x,y)reshape为(x*y,1)的函数
    '''
    flat_mfcc = np.empty([config.dataset_setting.MFCC_EIGENVALUE_AMOUNT * config.dataset_setting.MFCC_DATAFRAME_AMOUNT,], dtype = float, order = 'C')
    # 翻转mfcc数组
    # 原来的mfcc数组是mfcc特征值为行，以数据帧为列，用一维下标只能访问到某个mfcc特征值在各个数据帧下的取值，
    # 但我们需要方便地获取某个数据帧的各个mfcc特征值的取值，
    # 故翻转mfcc数组，使之以mfcc特征值为行，以数据帧为列，用一维下标可以访问到某个数据帧的各个mfcc特征值的取值
    transposed_aligned_mfcc = np.transpose(aligned_mfcc)
    # 进行reshape
    # 将每一帧的各个mfcc特征变量抽取出来，平放到输出数组中
    for i in range(0,config.dataset_setting.MFCC_DATAFRAME_AMOUNT):# 处理每一帧
        for j in range(0,config.dataset_setting.MFCC_EIGENVALUE_AMOUNT): # 针对某一帧，取出它的所有mfcc特征值
            if i < len(transposed_aligned_mfcc) and j < len(transposed_aligned_mfcc[0]):
                flat_mfcc[i*config.dataset_setting.MFCC_EIGENVALUE_AMOUNT+j] = transposed_aligned_mfcc[i][j]
            else:
                flat_mfcc[i*config.dataset_setting.MFCC_EIGENVALUE_AMOUNT+j] = 0
    return flat_mfcc

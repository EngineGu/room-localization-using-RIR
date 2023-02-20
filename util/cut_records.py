import numpy as np

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io


def cut_one_orientation_record_into_sample_records(orientation_record,sample_amount):
    """将一段录音音频的粒度从“取向”裁剪为“单次采样”,将取向粒度的音频裁剪为样本粒度的音频
    """

    search_area = orientation_record[0:round(len(orientation_record)/10)]  # 截取出前几个实验片段的大致范围，用于与mls做互相关确定第一个实验片段的起始点，此处取前10%的音频片段
    cross_correlation_of_mls_and_recording = np.correlate(search_area,config.file_io.MLS_SIGNAL,'valid')
    first_sample_start = np.where(cross_correlation_of_mls_and_recording > np.max(cross_correlation_of_mls_and_recording)*0.9)[0][0] # 将第一个实验片段与mls做互相关，其第一个接近最大值的位置就对应第一个实验片段的起始点

    start_points_of_samples = []
    end_points_of_samples = []
    for i in range(0,sample_amount):
        start_points_of_samples.append(first_sample_start + i * (config.exp_setting.INTERVAL_LENGTH + config.exp_setting.MLS_SIGNAL_LENGTH)) # 起始点之间间隔固定为：实验片段长度+片段间间隔长度
    for i in range(0,sample_amount):
        end_points_of_samples.append(int(start_points_of_samples[i] + config.exp_setting.MLS_SIGNAL_LENGTH)) # 各片段的组成为MLS播放的长度+余响的长度，即slice的主体+拖尾，故结束点的位置就是起始点位置+slice主体长+拖尾长
    
    sample_records = []
    for i in range(0,sample_amount):
        sample_i = orientation_record[start_points_of_samples[i]:end_points_of_samples[i]]
        sample_records.append(sample_i)
    return(sample_records)

def cut_orientation_records_into_sample_records(room_records_in_orientations,sample_amount):
    """对一个房间中所有位置点的所有取向的音频的每次采样裁剪出来,即对房间中每个位置点上每个取向的音频按采样次序切割成40段音频
    """
    room_records_in_samples = []
    for location_no in range(0,len(room_records_in_orientations)):
        location_records = []
        for orientation_no in range(0,len(room_records_in_orientations[location_no])):
            orientation_records = cut_one_orientation_record_into_sample_records(
                room_records_in_orientations[location_no][orientation_no],sample_amount)
            location_records.append(orientation_records)
        room_records_in_samples.append(location_records)
    return room_records_in_samples


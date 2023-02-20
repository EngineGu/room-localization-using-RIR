import numpy as np
import math
import heapq

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import util.file_io

def cir_cross_correlate(mls_siganl, sample_record):
    """循环互相关:
    要求数组mls与数组record的长度一样长
    """
    repeated_mls = np.concatenate(
        (mls_siganl[int(len(mls_siganl)/2):],
        mls_siganl,mls_siganl,mls_siganl,
        mls_siganl[:int(len(mls_siganl)/2)])
        )
    correlation = np.correlate(repeated_mls,sample_record,'valid')
    correlation = correlation / np.max(correlation)
    return correlation[::-1]

def calculate_rir_from_sample_record(sample_record):
    WINDOW_SIZE_FRONT = int(config.exp_setting.MLS_SIGNAL_LENGTH/1500) # 用于比较的窗口大小。在算法中通过均值法与拐点法进行自适应
    WINDOW_STEP_FRONT = int(config.exp_setting.MLS_SIGNAL_LENGTH/3000) # 窗口移动速度,即步长
    ABSOLUTE_ENERGY_THRESHOLD_RADIO_FRONT = 0.1 # 在所有energy中排前 ABSOLUTE_ENERGY_THRESHOLD_RADIO的
    WINDOW_SIZE_BACK = int(config.exp_setting.MLS_SIGNAL_LENGTH/150) # 用于比较的窗口大小。在算法中通过均值法与拐点法进行自适应
    WINDOW_STEP_BACK = int(config.exp_setting.MLS_SIGNAL_LENGTH/300) # 窗口移动速度,即步长
    ABSOLUTE_ENERGY_THRESHOLD_RADIO_BACK = 0.1 # 在所有energy中排后 1-ABSOLUTE_ENERGY_THRESHOLD_RADIO的

    PIR = cir_cross_correlate(config.file_io.MLS_SIGNAL,sample_record)
    climax_index = np.argwhere(PIR == np.max(PIR))[1][0]
    #######
    energy_of_windows = []
    for windows_open_position in range(climax_index,int(climax_index-config.exp_setting.MLS_SIGNAL_LENGTH/10),-WINDOW_STEP_FRONT):
        window = PIR[windows_open_position-WINDOW_SIZE_FRONT:windows_open_position]
        energy_of_window = 0.0
        for i in range(0,len(window)):
            energy_of_window += math.pow(window[i],2)
        energy_of_window = energy_of_window / WINDOW_SIZE_FRONT # 对窗口能量做归一化
        energy_of_windows.append(energy_of_window)

    largest_many_percent_energy_array = heapq.nlargest(int(len(energy_of_windows) * ABSOLUTE_ENERGY_THRESHOLD_RADIO_FRONT),energy_of_windows)
    absolute_energy_threshold = min(largest_many_percent_energy_array)

    cut_windows_index = len(energy_of_windows) - 3
    for i in range(0,len(energy_of_windows)-2):
        # 如果连续三个点在能量排名中低于前10%(即连续三个点在能量排名中排后90%)，就进行截取
        if (energy_of_windows[i] <= absolute_energy_threshold and energy_of_windows[i+1] <= absolute_energy_threshold and energy_of_windows[i+2] <= absolute_energy_threshold):
            cut_windows_index = i
            break
    energy_of_cut_window = energy_of_windows[cut_windows_index]

    cut_index_front = climax_index - WINDOW_STEP_FRONT * cut_windows_index
    ##############

    #######
    energy_of_windows = []
    for windows_open_position in range(climax_index,climax_index+config.exp_setting.MLS_SIGNAL_LENGTH,WINDOW_STEP_BACK):
        window = PIR[windows_open_position:windows_open_position+WINDOW_SIZE_BACK]
        energy_of_window = 0.0
        for i in range(0,len(window)):
            energy_of_window += math.pow(window[i],2)
        energy_of_window = energy_of_window / WINDOW_SIZE_BACK # 对窗口能量做归一化
        energy_of_windows.append(energy_of_window)

    largest_many_percent_energy_array = heapq.nlargest(int(len(energy_of_windows) * ABSOLUTE_ENERGY_THRESHOLD_RADIO_BACK),energy_of_windows)
    absolute_energy_threshold = min(largest_many_percent_energy_array)

    cut_windows_index = len(energy_of_windows) - 3
    for i in range(0,len(energy_of_windows)-2):
        # 如果连续三个点在能量排名中低于前99%(即连续三个点在能量排名中排后10%)，就进行截取
        if (energy_of_windows[i] <= absolute_energy_threshold and energy_of_windows[i+1] <= absolute_energy_threshold and energy_of_windows[i+2] <= absolute_energy_threshold):
            cut_windows_index = i
            break
    energy_of_cut_window = energy_of_windows[cut_windows_index]

    cut_index_back = climax_index + WINDOW_STEP_BACK * cut_windows_index
    ##############

    RIR = PIR[cut_index_front:cut_index_back]
    # # 对齐RIR
    # if (len(RIR) < config.exp_setting.MLS_SIGNAL_LENGTH):
    #     padding_length = config.exp_setting.MLS_SIGNAL_LENGTH - len(RIR)
    #     padding_zeros = np.zeros(padding_length,np.float32)
    #     RIR = np.concatenate((RIR,padding_zeros))
    # else:
    #     RIR = RIR[0:config.exp_setting.MLS_SIGNAL_LENGTH]

    # drawingboard = plt.figure()
    # plt.plot(RIR)
    # plt.title("RIR (N=15, L=32767)")
    # plt.xlabel("Number of samples, fp = 48k[Hz]")
    # plt.show()
    return RIR

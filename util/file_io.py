import librosa
import soundfile as sf
import pickle
import numpy as np

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io

def get_wav_file_path(data_folder_path,place_type,place_no,location_no,orientation_no,sample_no=0):
    '''将参数拼接成录音的.wav文件系统路径名字符串

    Args:
        data_folder: ".//data//raw_data//exp20210114_HW_Quiet_Strong_Unchanged//"
        place_no: 203
        location_no: 1
        orientation_no: 3

    Return:
        .//data//raw_data//exp20210114_HW_Quiet_Strong_Unchanged//Room_203_Location_1_Orientation_1.wav
    '''

    if place_type == "Room":
        file_path = data_folder_path + config.file_io.MLS_RECORD_FILENAME_PART_Room + str(place_no)
    elif place_type == "Corridor":
        file_path = data_folder_path + config.file_io.MLS_RECORD_FILENAME_PART_Corridor + str(place_no)
    else:
        raise Exception("place_type只能为Room或Corridor")

    file_path += config.file_io.MLS_RECORD_FILENAME_PART_Location + str(location_no)\
        + config.file_io.MLS_RECORD_FILENAME_PART_Orientation + str(orientation_no)


    if sample_no > 0:
        file_path += config.file_io.MLS_RECORD_FILENAME_PART_Sample + str(sample_no)
    
    file_path += config.file_io.MLS_RECORD_FILENAME_PART_Extension_WAV

    return file_path

def load_room_wave_files_in_orientations(data_folder,place_type,place_no,location_amount,orientation_amount):
    """以取向为粒度读入录音,将某个房间录音从文件系统中转化为内存中的3维数组
    """
    room_files_in_orientations = []
    for location_no in range(1,location_amount+1):
        location_files = []
        for orientation_no in range(1,orientation_amount+1):
            orientation_file_dir = get_wav_file_path(
                data_folder,place_type,place_no,location_no,orientation_no)
            orientation_file,_ = librosa.load(orientation_file_dir,config.exp_setting.SAMPLE_RATE)
            location_files.append(orientation_file)
        room_files_in_orientations.append(location_files)
    return room_files_in_orientations

def load_room_wav_files_in_samples(data_folder,place_type,place_no,location_amount,orientation_amount,sample_amount):
    """以采样为粒度读入录音,将某个房间录音从文件系统中转化为内存中的4维数组
    """
    room_files_in_samples = []
    for location_no in range(1,location_amount+1):
        location_files = []
        for orientation_no in range(1,orientation_amount+1):
            orientation_files = []
            for sample_no in range(1,sample_amount+1):
                sample_file_dir = get_wav_file_path(
                data_folder,place_type,place_no,location_no,orientation_no,sample_no)
                sample_file,_ = librosa.load(sample_file_dir,config.exp_setting.SAMPLE_RATE)
                orientation_files.append(sample_file)
            location_files.append(orientation_files)
        room_files_in_samples.append(location_files)
    return room_files_in_samples

def save_room_wav_files_in_samples(room_files_in_samples,data_folder_path,place_type,place_no):
    """以采样为粒度保存一个房间的录音,将某个房间中每个位置每个取向每个时间片段的录音保存成一个录音文件，存到文件系统中       
    """
    for location_no in range(0,len(room_files_in_samples)):# i+1:位置号
        for orientation_no in range(0,len(room_files_in_samples[location_no])):# j+1取向号
            for sample_no in range(0,len(room_files_in_samples[location_no][orientation_no])):
                sample_file_path = get_wav_file_path(data_folder_path,place_type,
                    place_no,location_no+1,orientation_no+1,sample_no+1)
                sf.write(sample_file_path, room_files_in_samples[location_no][orientation_no][sample_no], config.exp_setting.SAMPLE_RATE)
    return 0

def get_pkl_file_path(data_folder_path,place_type,place_no,location_no,orientation_no,sample_no=0):
    '''将参数拼接成录音的.pkl文件系统路径名字符串

    Args:
        data_folder: ".//data//raw_data//exp20210114_HW_Quiet_Strong_Unchanged//"
        place_no: 203
        location_no: 1
        orientation_no: 3

    Return:
        .//data//raw_data//exp20210114_HW_Quiet_Strong_Unchanged//Room_203_Location_1_Orientation_1.wav
    '''

    if place_type == "Room":
        file_path = data_folder_path + config.file_io.MLS_RECORD_FILENAME_PART_Room + str(place_no)
    elif place_type == "Corridor":
        file_path = data_folder_path + config.file_io.MLS_RECORD_FILENAME_PART_Corridor + str(place_no)
    else:
        raise Exception("place_type只能为Room或Corridor")

    file_path += config.file_io.MLS_RECORD_FILENAME_PART_Location + str(location_no)\
        + config.file_io.MLS_RECORD_FILENAME_PART_Orientation + str(orientation_no)


    if sample_no > 0:
        file_path += config.file_io.MLS_RECORD_FILENAME_PART_Sample + str(sample_no)
    
    file_path += config.file_io.MLS_RECORD_FILENAME_PART_Extension_PKL

    return file_path

def save_sample_pql_file(file_path,sample_data):
    '''保存一个采样的数据为二进制文件
    '''
    write_flow = open(file_path,"wb")
    pickle.dump(sample_data,write_flow)
    write_flow.close()
    return 0

def load_sample_pql_file(file_path):
    '''加载一个二进制格式的采样文件到内存中
    '''
    read_flow = open(file_path,"rb")
    sample_data = pickle.load(read_flow)
    read_flow.close()
    return sample_data

def load_room_pql_files_in_samples(data_folder,place_type,place_no,location_amount,orientation_amount,sample_amount):
    """以采样为粒度读入pkl文件,将某个房间录音从文件系统中转化为内存中的4维数组
    """
    room_files_in_samples = []
    for location_no in range(1,location_amount+1):
        location_files = []
        for orientation_no in range(1,orientation_amount+1):
            orientation_files = []
            for sample_no in range(1,sample_amount+1):
                sample_file_dir = get_pkl_file_path(
                data_folder,place_type,place_no,location_no,orientation_no,sample_no)
                sample_file = load_sample_pql_file(sample_file_dir)
                orientation_files.append(sample_file)
            location_files.append(orientation_files)
        room_files_in_samples.append(location_files)
    return room_files_in_samples

def get_txt_file_path_in_dataset_conditions(
    data_folder,dataset_condition,leave_type,localization_level,dataset_type):
    if dataset_type == "train_data":
        dataset_type_str = "train_data"
    elif dataset_type == "train_label":
        dataset_type_str = "train_label"
    elif dataset_type == "test_data":
        dataset_type_str = "test_data"
    elif dataset_type == "test_label":
        dataset_type_str = "test_label"
    else:
        raise Exception("dataset_type必须为train_data或train_label或test_data或test_label")
        
    path_str = data_folder\
        + dataset_condition\
        + "_" + leave_type\
        + "_" + localization_level\
        + "_" + dataset_type_str\
        + ".dat"
    
    return path_str
 
def save_txt_files_in_dataset_conditions(train_data,train_label,test_data,test_label,
    data_folder,dataset_condition,orientation_amount,sample_amount,leave_type,localization_level):
    # 存train_data
    train_data_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"train_data"
    )
    np.savetxt(train_data_file_path, train_data)
    # 存train_label
    train_label_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"train_label"
    )
    np.savetxt(train_label_file_path, train_label)
    # 存test_data
    test_data_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"test_data"
    )
    np.savetxt(test_data_file_path, test_data)
    # 存test_label
    test_label_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"test_label"
    )
    np.savetxt(test_label_file_path, test_label)
    return 0

def load_txt_files_in_dataset_conditions(
    data_folder,dataset_condition,leave_type,localization_level):
    # 读train_data
    train_data_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"train_data"
    )
    train_data = np.loadtxt(train_data_file_path)
    # 读train_label
    train_label_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"train_label"
    )
    train_label = np.loadtxt(train_label_file_path)
    # 读test_data
    test_data_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"test_data"
    )
    test_data = np.loadtxt(test_data_file_path)
    # 读test_label
    test_label_file_path = get_txt_file_path_in_dataset_conditions(
        data_folder,dataset_condition,leave_type,localization_level,"test_label"
    )
    test_label = np.loadtxt(test_label_file_path)
    return train_data,train_label,test_data,test_label

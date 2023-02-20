import soundfile as sf

import sys
sys.path.append('../')

import config.exp_setting
import config.file_io
import config.dataset_setting

import util.cut_records
import util.file_io
import util.rir
import util.mfcc
import util.dataset

for processing_condition in range(0,len(config.exp_setting.EXP_CONDITION)):
    print(config.exp_setting.EXP_CONDITION[processing_condition])
    load_data_folder = config.file_io.MLS_RECORD_IN_SAMPLES_PATH_IN_EXP_CONDITION[processing_condition]
    write_data_folder = config.file_io.REAL_RIR_PATH_IN_EXP_CONDITION[processing_condition]
    place_identifier = config.exp_setting.EXP_PLACE_IDENTIFIER_IN_CONDITION[processing_condition]
    for i in range(0,len(place_identifier)):
        # 获取该房间的采样粒度的录音
        place_type = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["place_type"]
        place_no = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["place_no"]
        location_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["location_amount"]
        orientation_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["orientation_amount"]
        sample_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["sample_amount"]
        room_records_in_samples = util.file_io.load_room_wav_files_in_samples(
            load_data_folder, place_type, place_no, location_amount, orientation_amount, sample_amount)
        # 计算各采样录音的rir并存储
        for location_no in range(0,location_amount):
            for orientation_no in range(0,orientation_amount):
                for sample_no in range(0,sample_amount):
                    sample_record = room_records_in_samples[location_no][orientation_no][sample_no]
                    rir_of_sample_record = util.rir.calculate_rir_from_sample_record(sample_record)
                    rir_of_sample_record_path = util.file_io.get_wav_file_path(
                        write_data_folder,place_type, place_no,location_no+1,orientation_no+1,sample_no+1)
                    sf.write(rir_of_sample_record_path, rir_of_sample_record, config.exp_setting.SAMPLE_RATE)



for processing_condition in range(0,len(config.exp_setting.EXP_CONDITION)):
    print(config.exp_setting.EXP_CONDITION[processing_condition])
    load_data_folder = config.file_io.REAL_RIR_PATH_IN_EXP_CONDITION[processing_condition]
    write_data_folder = config.file_io.MFCC_PATH_IN_EXP_CONDITION[processing_condition]
    place_identifiers = config.exp_setting.EXP_PLACE_IDENTIFIER_IN_CONDITION[processing_condition]
    for i in range(0,len(place_identifiers)):
        # 获取该房间的采样粒度的录音的RIR
        place_type = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["place_type"]
        place_no = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["place_no"]
        location_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["location_amount"]
        orientation_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["orientation_amount"]
        sample_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["sample_amount"]
        room_rirs_in_samples = util.file_io.load_room_wav_files_in_samples(
            load_data_folder, place_type, place_no, location_amount, orientation_amount, sample_amount)
        # 计算各采样录音的rir的mfcc,展平后存储
        for location_no in range(0,location_amount):
            for orientation_no in range(0,orientation_amount):
                for sample_no in range(0,sample_amount):
                    # 读取rir
                    sample_rir = room_rirs_in_samples[location_no][orientation_no][sample_no]
                    # 计算rir的mfcc
                    mfcc_of_rir = util.mfcc.get_mfcc_of_sample_rir(sample_rir)
                    # 展平mfcc
                    flat_mfcc_of_rir = util.mfcc.flatten_mfcc(mfcc_of_rir)
                    # 存储mfcc
                    sample_mfcc_path = util.file_io.get_pkl_file_path(
                        write_data_folder,place_type, place_no,location_no+1,orientation_no+1,sample_no+1)
                    util.file_io.save_sample_pql_file(sample_mfcc_path,flat_mfcc_of_rir)

for processing_condition in range(0,len(config.dataset_setting.DATASET_CONDITION)):
    print(config.dataset_setting.DATASET_CONDITION[processing_condition])
    # sample, room总表
    lsrl_train_data = []
    lsrl_train_label = []
    lsrl_test_data = []
    lsrl_test_label = []
    # sample, location总表
    lsll_train_data = []
    lsll_train_label = []
    lsll_test_data = []
    lsll_test_label = []
    # orientation, room总表
    lorl_train_data = []
    lorl_train_label = []
    lorl_test_data = []
    lorl_test_label = []
    # orientation, location总表
    loll_train_data = []
    loll_train_label = []
    loll_test_data = []
    loll_test_label = []
    # location, room总表
    llrl_train_data = []
    llrl_train_label = []
    llrl_test_data = []
    llrl_test_label = []
    load_data_folder = config.file_io.MFCC_PATH_IN_DATASET_CONDITION[processing_condition]
    write_data_folder = config.file_io.DATASET_PARENT_PATH
    place_identifiers = config.dataset_setting.DATASET_PLACE_IDENTIFIER_IN_CONDITION[processing_condition]
    for i in range(0,len(place_identifiers)):
        # 获取该房间的各次采样的mfcc
        place_type = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["place_type"]
        place_no = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["place_no"]
        location_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["location_amount"]
        
        dataset_orientation_amount = config.dataset_setting.DATASET_ORIENTATION_AMOUNT_IN_CONDITION[processing_condition]
        dataset_sample_amount = config.dataset_setting.DATASET_SAMPLE_AMOUNT_IN_CONDITION[processing_condition]
        
        room_mfcces_in_samples = util.file_io.load_room_pql_files_in_samples(
            load_data_folder, place_type, place_no, location_amount, 4, dataset_sample_amount) # 此处取向数据应取全
        # 获取房间的leave samples，room level的数据集并添加到总表中
        train_data,train_label,test_data,test_label = util.dataset.get_leave_samples_data_label(
            room_mfcces_in_samples,place_type,place_no,location_amount,dataset_orientation_amount,dataset_sample_amount,"room_level"
        )
        lsrl_train_data += train_data
        lsrl_train_label += train_label
        lsrl_test_data += test_data
        lsrl_test_label += test_label
        # 获取leave samples，location level的数据集并保存
        train_data,train_label,test_data,test_label = util.dataset.get_leave_samples_data_label(
            room_mfcces_in_samples,place_type,place_no,location_amount,dataset_orientation_amount,dataset_sample_amount,"location_level"
        )
        lsll_train_data += train_data
        lsll_train_label += train_label
        lsll_test_data += test_data
        lsll_test_label += test_label
        # 获取leave 1 orientation，room level的数据集并保存
        train_data,train_label,test_data,test_label = util.dataset.get_leave_1_orientation_data_label(
            room_mfcces_in_samples,place_type,place_no,location_amount,dataset_orientation_amount,dataset_sample_amount,"room_level"
        )
        lorl_train_data += train_data
        lorl_train_label += train_label
        lorl_test_data += test_data
        lorl_test_label += test_label
        # 获取leave 1 orientation，location level的数据集并保存
        train_data,train_label,test_data,test_label = util.dataset.get_leave_1_orientation_data_label(
            room_mfcces_in_samples,place_type,place_no,location_amount,dataset_orientation_amount,dataset_sample_amount,"location_level"
        )
        loll_train_data += train_data
        loll_train_label += train_label
        loll_test_data += test_data
        loll_test_label += test_label
        # 获取leave 1 location，room level的数据集并保存
        train_data,train_label,test_data,test_label = util.dataset.get_leave_1_location_data_label(
            room_mfcces_in_samples,place_type,place_no,location_amount,dataset_orientation_amount,dataset_sample_amount,"room_level"
        )
        llrl_train_data += train_data
        llrl_train_label += train_label
        llrl_test_data += test_data
        llrl_test_label += test_label
    util.file_io.save_txt_files_in_dataset_conditions(
        lsrl_train_data,lsrl_train_label,lsrl_test_data,lsrl_test_label,
        config.file_io.DATASET_PARENT_PATH,config.dataset_setting.DATASET_CONDITION[processing_condition],
        dataset_orientation_amount,dataset_sample_amount,"leave_samples","room_level")
    util.file_io.save_txt_files_in_dataset_conditions(
        lsll_train_data,lsll_train_label,lsll_test_data,lsll_test_label,
        config.file_io.DATASET_PARENT_PATH,config.dataset_setting.DATASET_CONDITION[processing_condition],
        dataset_orientation_amount,dataset_sample_amount,"leave_samples","location_level")
    util.file_io.save_txt_files_in_dataset_conditions(
        lorl_train_data,lorl_train_label,lorl_test_data,lorl_test_label,
        config.file_io.DATASET_PARENT_PATH,config.dataset_setting.DATASET_CONDITION[processing_condition],
        dataset_orientation_amount,dataset_sample_amount,"leave_1_orientation","room_level")
    util.file_io.save_txt_files_in_dataset_conditions(
        loll_train_data,loll_train_label,loll_test_data,loll_test_label,
        config.file_io.DATASET_PARENT_PATH,config.dataset_setting.DATASET_CONDITION[processing_condition],
        dataset_orientation_amount,dataset_sample_amount,"leave_1_orientation","location_level")
    util.file_io.save_txt_files_in_dataset_conditions(
        llrl_train_data,llrl_train_label,llrl_test_data,llrl_test_label,
        config.file_io.DATASET_PARENT_PATH,config.dataset_setting.DATASET_CONDITION[processing_condition],
        dataset_orientation_amount,dataset_sample_amount,"leave_1_location","room_level")
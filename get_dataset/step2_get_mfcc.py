import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import util.cut_records
import util.file_io
import util.rir
import util.mfcc

for processing_condition in range(len(config.exp_setting.EXP_CONDITION)-1,len(config.exp_setting.EXP_CONDITION)):
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

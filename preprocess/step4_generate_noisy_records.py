import soundfile as sf
import pickle

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import util.cut_records
import util.file_io
import util.rir
import util.mfcc
import util.generate_records


load_data_folder = config.file_io.REAL_RIR_PATH_IN_EXP_CONDITION[5]
write_data_folder = config.file_io.MLS_RECORD_IN_SAMPLES_PATH_IN_EXP_CONDITION[6]
place_identifiers = config.exp_setting.EXP_PLACE_IDENTIFIER_IN_CONDITION[5]
for i in range(0,len(place_identifiers)):
    # 获取该房间的采样粒度的录音的RIR
    place_type = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["place_type"]
    place_no = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["place_no"]
    location_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["location_amount"]
    orientation_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["orientation_amount"]
    sample_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifiers[i]]["sample_amount"]
    room_rirs_in_samples = util.file_io.load_room_wav_files_in_samples(
        load_data_folder, place_type, place_no, location_amount, orientation_amount, sample_amount)
    # 利用各采样录音的rir的计算mls录音音频后存储
    for location_no in range(0,location_amount):
        for orientation_no in range(0,orientation_amount):
            for sample_no in range(0,sample_amount):
                # 读取rir
                sample_rir = room_rirs_in_samples[location_no][orientation_no][sample_no]
                # 获取噪音
                noise_slice = util.generate_records.generate_noise()
                # 生成带噪的mls录音
                noisy_sample_record = util.generate_records.generate_mls_record_in_samples(
                    sample_rir,config.file_io.MLS_SIGNAL,noise_slice
                )
                # 存储带噪的mls录音
                noisy_sample_record_path = util.file_io.get_wav_file_path(
                    write_data_folder,place_type, place_no,location_no+1,orientation_no+1,sample_no+1)
                sf.write(noisy_sample_record_path,noisy_sample_record,config.exp_setting.SAMPLE_RATE)
import soundfile as sf

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import util.cut_records
import util.file_io
import util.rir

for processing_condition in range(len(config.exp_setting.EXP_CONDITION)-1,len(config.exp_setting.EXP_CONDITION)):
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

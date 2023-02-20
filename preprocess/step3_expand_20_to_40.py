import librosa
import soundfile as sf

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import util.cut_records
import util.file_io

for processing_condition in range(0,len(config.exp_setting.EXP_CONDITION)):
    print(config.exp_setting.EXP_CONDITION[processing_condition])
    load_data_folder = config.file_io.MLS_RECORD_IN_SAMPLES_PATH_IN_EXP_CONDITION[processing_condition]
    write_data_folder = config.file_io.MLS_RECORD_IN_SAMPLES_PATH_IN_EXP_CONDITION[processing_condition]
    place_identifier = config.exp_setting.EXP_PLACE_IDENTIFIER_IN_CONDITION[processing_condition]
    for i in range(0,len(place_identifier)):
        place_type = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["place_type"]
        place_no = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["place_no"]
        location_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["location_amount"]
        orientation_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["orientation_amount"]
        sample_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["sample_amount"]

        for location_no in range(1,location_amount+1):
            for orientation_no in range(1,orientation_amount+1):
                for sample_no in range(1,sample_amount+1):
                    read_sample_record_path = util.file_io.get_wav_file_path(
                        load_data_folder,place_type,place_no,location_no,orientation_no,sample_no)
                    sample_record,_ = librosa.load(read_sample_record_path,config.exp_setting.SAMPLE_RATE)
                    write_sample_record_path = util.file_io.get_wav_file_path(
                        write_data_folder,place_type, place_no,location_no,orientation_no,sample_no+20)
                    sf.write(write_sample_record_path, sample_record, config.exp_setting.SAMPLE_RATE)


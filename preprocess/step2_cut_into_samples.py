import sys
sys.path.append('../')
import config.exp_setting
import config.file_io
import util.cut_records
import util.file_io

for processing_condition in range(0,len(config.exp_setting.EXP_CONDITION)):
    print(config.exp_setting.EXP_CONDITION[processing_condition])
    load_data_folder = config.file_io.MLS_RECORD_IN_ORIENTATIONS_PATH_IN_EXP_CONDITION[processing_condition]
    write_data_folder = config.file_io.MLS_RECORD_IN_SAMPLES_PATH_IN_EXP_CONDITION[processing_condition]
    place_identifier = config.exp_setting.EXP_PLACE_IDENTIFIER_IN_CONDITION[processing_condition]
    for i in range(0,len(place_identifier)):
        place_type = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["place_type"]
        place_no = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["place_no"]
        location_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["location_amount"]
        orientation_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["orientation_amount"]
        room_records_in_orientations = util.file_io.load_room_wave_files_in_orientations(
            load_data_folder,place_type,place_no,location_amount,orientation_amount)
    
        sample_amount = config.exp_setting.EXP_PLACE_CONFIG[place_identifier[i]]["sample_amount"]
        room_records_in_samples = util.cut_records.cut_orientation_records_into_sample_records(
            room_records_in_orientations,sample_amount)
    
        util.file_io.save_room_wav_files_in_samples(
            room_records_in_samples,write_data_folder,place_type,place_no)

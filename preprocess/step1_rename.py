import librosa
import soundfile as sf

# 实验设置参数
room_no = "203"
location_amount = 2
orientation_amount = 4
SAMPLE_RATE = 48000
# 文件系统参数
# 读出文件
READ_FOLDER = "D:\\Code\\mlsLocalization\\data\\RIR_MLS_EXP\\"
READ_ROOM_STR = "Room_"
READ_LOCATION_STR = "_Location_"
READ_ORIENTATION_STR = "_Orientation_"
READ_RECORD_FILE_EXTENSION_NAME = ".wav"
# 写入文件
WRITE_FOLDER = "D:\\Code\\mlsLocalization\\data\\exp20220330_HW_Quiet_Strong_Unchanged\\"
WRITE_ROOM_STR = "Room_"
WRITE_LOCATION_STR = "_Location_"
WRITE_ORIENTATION_STR = "_Orientation_"
WRITE_RECORD_FILE_EXTENSION_NAME = ".wav"

for location in range(1,location_amount+1):
    for orientation in range(1,orientation_amount+1):
        record_path = READ_FOLDER + READ_ROOM_STR  + str(room_no) + READ_LOCATION_STR + str(location)\
            + READ_ORIENTATION_STR + str(orientation) + READ_RECORD_FILE_EXTENSION_NAME
        orientation_records,_ = librosa.load(record_path, sr = SAMPLE_RATE)
        output_path = WRITE_FOLDER + WRITE_ROOM_STR + str("East") + WRITE_LOCATION_STR + str(location) + WRITE_ORIENTATION_STR + str(orientation) + WRITE_RECORD_FILE_EXTENSION_NAME
        sf.write(output_path, orientation_records, SAMPLE_RATE)
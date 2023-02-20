
## MFCC参数
MFCC_EIGENVALUE_AMOUNT = 20 # 个；MFCC特征值数量
MFCC_DATAFRAME_AMOUNT = 6 # 帧；MFCC的数据帧数量，由rir的长度决定，当RIR长度为32767时，MFCC数据帧数量为64

## 四、数据集条件相关参数
### (一)数据集条件的名称
DATASET_CONDITION = [
    "exp20210114_HW_Quiet_Strong_Unchanged_orientation_4_sample_40", # condition 0
    "exp20210716_OP_Noisy_Strong_Unchanged_orientation_4_sample_40", # condition 1
    "exp20210716_OP_Quiet_Strong_Unchanged_orientation_4_sample_40", # condition 2
    "exp20210716_OP_Quiet_Weak_Unchanged_orientation_4_sample_40",   # condition 3
    "exp20220330_HW_Quiet_Strong_Changed_orientation_4_sample_40",   # condition 4
    "exp20220330_HW_Quiet_Strong_Unchanged_orientation_4_sample_40", # condition 5
    "exp20220330_HW_Quiet_Strong_Unchanged_orientation_2_sample_20", # condition 6
    "exp20220330_HW_Quiet_Strong_Unchanged_orientation_4_sample_20", # condition 7
    "exp20220330_HW_Quiet_Strong_Unchanged_orientation_2_sample_40", # condition 8
    "exp20220330_HW_Noisy_Strong_Unchanged_orientation_4_sample_40", # condition 9
]
###（二）不同数据集条件下的实验场所
DATASET_PLACE_IDENTIFIER_IN_CONDITION = [
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_213","Room_222"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"]
]
###（三）不同数据集条件下的取向数
DATASET_ORIENTATION_AMOUNT_IN_CONDITION = [
    4,
    4,
    4,
    4,
    4,
    4,
    2,
    4,
    2,
    4,
]
###（四）不同数据集条件下的采样数
DATASET_SAMPLE_AMOUNT_IN_CONDITION = [
    40,
    40,
    40,
    40,
    40,
    40,
    20,
    20,
    40,
    40,
]

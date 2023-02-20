# 实验设置参数
## 一、MLS信号音频参数
SAMPLE_RATE = 48000 # MLS与录音音频的采样频率，本实验中取的是48kHZ，也意味着1s的采样点数为48000
MLS_SIGNAL_LENGTH = 32767 # 一个实验片段主体的长度，与mls音频长度一样。单位为采样点。MLS的性质就是长度为2^n - 1，此处MLS阶数为15，故长度为2^15 - 1 = 32767个采样点

## 二、MLS录音音频参数
INTERVAL_LENGTH = 48000 # 实验片段之间存在间隔，一个间隔长为1s，采样率为48kHz，故一个间隔长为48000采样点

## 三、实验场所参数
### （一）实验场所的名字
EXP_PLACE_IDENTIFIER = ["Corridor_1","Corridor_2","Corridor_3",\
    "Room_203","Room_204","Room_205","Room_209","Room_212",\
    "Room_213","Room_216","Room_222","Room_224"]
### （二）实验场所相关参数的名字
EXP_PLACE_PARAMETERS = ["place_type","place_no","location_amount","orientation_amount","sample_amount"]
### （三）实验场所对应的相关参数的值
EXP_PLACE_CONFIG = {
    EXP_PLACE_IDENTIFIER[0]:{
        EXP_PLACE_PARAMETERS[0]:"Corridor",
        EXP_PLACE_PARAMETERS[1]:1,
        EXP_PLACE_PARAMETERS[2]:4,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[1]:{
        EXP_PLACE_PARAMETERS[0]:"Corridor",
        EXP_PLACE_PARAMETERS[1]:2,
        EXP_PLACE_PARAMETERS[2]:4,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[2]:{
        EXP_PLACE_PARAMETERS[0]:"Corridor",
        EXP_PLACE_PARAMETERS[1]:3,
        EXP_PLACE_PARAMETERS[2]:2,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
   EXP_PLACE_IDENTIFIER[3]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:203,
        EXP_PLACE_PARAMETERS[2]:4,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
   EXP_PLACE_IDENTIFIER[4]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:204,
        EXP_PLACE_PARAMETERS[2]:2,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[5]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:205,
        EXP_PLACE_PARAMETERS[2]:4,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[6]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:209,
        EXP_PLACE_PARAMETERS[2]:6,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[7]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:212,
        EXP_PLACE_PARAMETERS[2]:8,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[8]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:213,
        EXP_PLACE_PARAMETERS[2]:8,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[9]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:216,
        EXP_PLACE_PARAMETERS[2]:8,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[10]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:222,
        EXP_PLACE_PARAMETERS[2]:4,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
    EXP_PLACE_IDENTIFIER[11]:{
        EXP_PLACE_PARAMETERS[0]:"Room",
        EXP_PLACE_PARAMETERS[1]:224,
        EXP_PLACE_PARAMETERS[2]:4,
        EXP_PLACE_PARAMETERS[3]:4,
        EXP_PLACE_PARAMETERS[4]:40,
    },
}

## 四、实验条件相关参数
### (一)实验条件的名称
EXP_CONDITION = [
    "exp20210114_HW_Quiet_Strong_Unchanged", # condition 0
    "exp20210716_OP_Noisy_Strong_Unchanged", # condition 1
    "exp20210716_OP_Quiet_Strong_Unchanged", # condition 2
    "exp20210716_OP_Quiet_Weak_Unchanged",   # condition 3
    "exp20220330_HW_Quiet_Strong_Changed",   # condition 4
    "exp20220330_HW_Quiet_Strong_Unchanged", # condition 5
    "exp20220330_HW_Noisy_Strong_Unchanged", # condition 6
]
###（二）不同实验条件下的实验场所
EXP_PLACE_IDENTIFIER_IN_CONDITION = [
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_205","Room_209","Room_212"],
    ["Room_203","Room_213","Room_222"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"],
    ["Corridor_1","Corridor_2","Corridor_3", "Room_203","Room_204","Room_205","Room_209","Room_212",
        "Room_213","Room_216","Room_222","Room_224"]
]
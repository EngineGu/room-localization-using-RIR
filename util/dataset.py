def get_label(place_type,place_no,location_no,localization_level):
    '''获取标签值
    '''
    # 走廊与房间标签不一样
    if place_type == "Corridor":
        place_no += 100
    elif place_type == "Room":
        place_no = place_no
    else:
        raise Exception("place_type只能为Corridor或Room")
    # 定位粒度不同，标签不一样
    if localization_level == "room_level":
        label = place_no
    elif localization_level == "location_level":
        label = place_no * 10 + (location_no + 1)
    else:
        raise Exception("localization_level必须为room_level或者location_level")
    return label

def get_inf_from_label(label):
    '''从标签值获取房间、位置信息
    '''
    if label < 200: # 走廊,room_level
        place_type = "Corridor"
        place_no = label - 100
        location_no = -1
    elif label < 1000: # 房间,room_level
        place_type = "Room"
        place_no = label
        location_no = -1
    elif label < 2000: # 走廊,location_level
        place_type = "Corridor"
        place_no = int(label/10) - 100
        location_no = label % 10
    elif label < 3000:# 房间,location_level
        place_type = "Room"
        place_no = int(label/10)
        location_no = label % 10
    if location_no == -1: # room_level
        inf_str = place_type + "_" + str(place_no)
    else: # location_level
        inf_str = place_type + "_" + str(place_no) + "_" +str(location_no)
    return inf_str

def get_leave_samples_data_label(
    room_mfcc,place_type,place_no, location_amount,orientation_amount,sample_amount,localization_level
    ):
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    for location_no in range(0,location_amount):
        # 根据orientation_amout选择退化与否
        if orientation_amount == 4:
            step = 1
        elif orientation_amount == 2:
            step = 2
        else:
            raise Exception("orientation_amount必须为4或者2")
        for orientation_no in range(0,len(room_mfcc[location_no]),step):
            # 根据sample_amount选择退化与否
            if sample_amount == 40:
                max = 40
            elif sample_amount == 20:
                max = 20
            else:
                raise Exception("sample_amount必须为40或者20")
            for sample_no in range(0,max):
                data = room_mfcc[location_no][orientation_no][sample_no]
                label = get_label(place_type,place_no,location_no,localization_level)
                # 填入数据和标签: 能被4整除的放测试集，其他放训练集，达到25%测试，75%训练的效果
                if (sample_no+1) % 4 == 0:
                    test_data.append(data)
                    test_label.append(label)
                else:
                    train_data.append(data)
                    train_label.append(label)
    return train_data,train_label,test_data,test_label

def get_leave_1_orientation_data_label(
    room_mfcc,place_type,place_no, location_amount,orientation_amount,sample_amount,localization_level
    ):
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    for location_no in range(0,location_amount):
        # 根据orientation_amout选择退化与否
        if orientation_amount == 4:
            step = 1
        elif orientation_amount == 2:
            step = 2
        else:
            raise Exception("orientation_amount必须为4或者2")
        for orientation_no in range(0,len(room_mfcc[location_no]),step):
            # 根据sample_amount选择退化与否
            if sample_amount == 40:
                max = 40
            elif sample_amount == 20:
                max = 20
            else:
                raise Exception("sample_amount必须为40或者20")
            for sample_no in range(0,max):
                data = room_mfcc[location_no][orientation_no][sample_no]
                label = get_label(place_type,place_no,location_no,localization_level)
                # 填入数据和标签:
                if orientation_no == 0: # 被leave的取向：全部进测试集
                    test_data.append(data)
                    test_label.append(label)
                else:# 其他取向：能被4整除的放测试集，其他放训练集，达到25%测试，75%训练的效果
                    if (sample_no+1) % 4 == 0:
                       test_data.append(data)
                       test_label.append(label)
                    else:
                        train_data.append(data)
                        train_label.append(label)
    return train_data,train_label,test_data,test_label

def get_leave_1_location_data_label(
    room_mfcc,place_type,place_no, location_amount,orientation_amount,sample_amount,localization_level
    ):
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    for location_no in range(0,location_amount):
        # 根据orientation_amout选择退化与否
        if orientation_amount == 4:
            step = 1
        elif orientation_amount == 2:
            step = 2
        else:
            raise Exception("orientation_amount必须为4或者2")
        for orientation_no in range(0,len(room_mfcc[location_no]),step):
            # 根据sample_amount选择退化与否
            if sample_amount == 40:
                max = 40
            elif sample_amount == 20:
                max = 20
            else:
                raise Exception("sample_amount必须为40或者20")
            for sample_no in range(0,max):
                data = room_mfcc[location_no][orientation_no][sample_no]
                label = get_label(place_type,place_no,location_no,"room_level") # leave 1 location的只能为房间粒度定位
                # 填入数据和标签:
                if location_no == 0: # 被leave的位置：全部进测试集
                    test_data.append(data)
                    test_label.append(label)
                else:# 其他位置：能被4整除的放测试集，其他放训练集，达到25%测试，75%训练的效果
                    if (sample_no+1) % 4 == 0:
                       test_data.append(data)
                       test_label.append(label)
                    else:
                        train_data.append(data)
                        train_label.append(label)
    return train_data,train_label,test_data,test_label
                


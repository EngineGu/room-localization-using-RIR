import numpy as np
import random

import sys
sys.path.append('../')
import config.exp_setting
import config.file_io

def generate_mls_record_in_samples(rir,mls,noise):
    fg_noise_record = np.convolve(noise,rir,"full")[0:config.exp_setting.MLS_SIGNAL_LENGTH]
    pure_mls_record = np.convolve(mls,rir,"full")[0:config.exp_setting.MLS_SIGNAL_LENGTH]
    final_mls_record = pure_mls_record + fg_noise_record
    return final_mls_record

def generate_noise():
    complete_noise = config.file_io.BABBLE_NOISE
    noise_slice_length = config.exp_setting.MLS_SIGNAL_LENGTH
    slice_start = random.randint(0, len(complete_noise)-noise_slice_length)
    noise_slice =  complete_noise[slice_start:slice_start+noise_slice_length]
    return noise_slice

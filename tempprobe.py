import os
import glob
import re

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

to_farenheit = lambda x: x * 1.8 + 32

def read_raw_temp():
    lines = ''
    with open(device_file, 'r') as f:
        lines = f.readlines() 
    return lines[1]

def get():
    temp = re.search('t=(\d+)', read_raw_temp())
    if temp:
        return to_farenheit(int(temp.group(1))/1000.0)

if __name__ == "__main__":
    print(get())

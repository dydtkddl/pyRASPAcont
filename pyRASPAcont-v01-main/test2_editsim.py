from pyrascont import *
import numpy as np
dir_list_n = []

with open('sim_dir_list.txt', 'r') as f:
    dir_list_n = f.readlines()
print(dir_list_n)

dir_list = []
for dirr in dir_list_n:
    dir_list.append(dirr[:-1])
print(dir_list)

P = [0.5E5, 1E5, 2E5]
T = [300, 310, 320]
fw = ['Cu-BTC',
        'MOF-200',
        'MIL-88A-open',]
for dirr, pp, tt, fww in zip(dir_list, P,T,fw):
    editsim(dirr, pp, tt, fww, [1, 1, 1], PrintResult=True)


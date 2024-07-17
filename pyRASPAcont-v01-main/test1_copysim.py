from pyrascont import *
import numpy as np
# %% Make copies of sim_origin

dir_list = copysim('sim_origin', 'sim_no', 3)
print(dir_list)

f = open('sim_dir_list.txt', 'w')
for dirr in dir_list:
    f.write(dirr+'\n')
f.close()



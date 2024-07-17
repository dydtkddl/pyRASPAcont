from pyrascont import *

f = open('sim_dir_list.txt') 

dir_list_n = f.readlines()
f.close()
dir_list = []
for dirr in dir_list_n:
    dir_list.append(dirr[:-1])

print(dir_list)

for dirr in dir_list:
    runsim(dirr)


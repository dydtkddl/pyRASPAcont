from pyrascont import *
import os

prefix = 'sim_no'
removesim(prefix)

for dirr in os.listdir():
    print(dirr)

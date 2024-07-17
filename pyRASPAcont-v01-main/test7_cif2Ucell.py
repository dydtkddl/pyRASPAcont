from pyrascont import *
import os

dir_home = os.getenv("HOME")
print(dir_home)

basepath = os.path.dirname(os.path.abspath(__file__))
cif_path = dir_home + '/Research/simulations/share/raspa/structures/cif/'
cif_file = 'MIL-88A-open'
#cif_file = 'Cu-BTC'
#cif_file = 'MOF-200'
cutoff = 14	# Angstrom

os.chdir(cif_path)
res_ucell = cif2Ucell(cif_file, cutoff, Display = True)
os.chdir(basepath)

print(res_ucell)

'''
This file takes in the txt file as filname and corr con file as output and replaces hba1c and type __num.
OUTPUT: samples dir
'''

import os
import time
import glob


outdir = "samples"
c =  1
for filename in glob.glob('temp1/*.txt'):
	print c
	temp = filename.split("/")[1]
	temp = temp.replace('txt', 'con')
	os.system("python parsing_hb.py "+filename+" "+outdir+"/"+temp)
	time.sleep(3)
	c += 1
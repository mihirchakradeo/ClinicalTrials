'''
This file takes in the txt file as filname and corr con file as output and adds bmi values to the con files
OUTPUT: con files in samples dir
'''

import os
import time
import glob


outdir = "samples"
c = 1
for filename in glob.glob('parsed_files/*.txt'):
	print c
	temp = filename.split("/")[1]
	temp = temp.replace('txt', 'con')
	os.system("python parsing_hb.py "+filename+" "+outdir+"/"+temp)
	time.sleep(2)
	c += 1

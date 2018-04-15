'''
This file takes the txt files and passes it on to cliner and writes con to samples dir
'''

import os
import time
import glob


outdir = "/samples"
c =  1
for filename in glob.glob('parsed_files/*.txt'):
	print c
	os.system("../../../cliner/CliNER/ ./cliner predict --txt "+filename+" --out "+outdir+" --model models/silver.crf --format i2b2")
	time.sleep(10)
	c += 1
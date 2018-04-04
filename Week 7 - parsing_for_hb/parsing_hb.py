'''
This script reads the clinical trials txt file which has the Inclusion and Exclusion criteria in it
and then scans for Hbg1Ac/Hb1AC
'''
import re
import sys


def get_values(fname, word):
	lines = []
	hba1c =  []
	with open(fname) as f:
		for line in f:
			if re.findall(word, line.lower()):
				hba1c.append(line)
	return hba1c


def extract_percentage(hba1c):
	hba1c_values = []
	
	for line in hba1c:
		if re.findall(r'\d+\D*%', line):
			hba1c_values.append(re.findall(r'\d+\D*%', line))
	return hba1c_values


def main():
	# Checking if file path is given or not
	if len(sys.argv) == 1:
		print "Usage: python ",sys.argv[0]," <path to txt>"
		sys.exit()

	fname = sys.argv[1]


	# Searching for hba1c and hga1c in the file
	hba1c = get_values(fname, "hba1c")
	print hba1c

	hga1c = get_values(fname, "hga1c")
	print hga1c

	# Now getting the exact percentage value of Hb1AC
	if hba1c:
		hba1c_values = extract_percentage(hba1c)[0][0]
		print hba1c_values

	# Now getting the exact percentage value of Hg1AC
	if hga1c:
		hga1c_values = extract_percentage(hga1c)[0][0]
		print hga1c_values


if __name__ == '__main__':
	main()
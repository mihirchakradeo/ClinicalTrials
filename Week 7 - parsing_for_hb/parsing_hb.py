'''
This script reads the clinical trials txt file which has the Inclusion and Exclusion criteria in it
and then scans for Hbg1Ac/Hb1AC
'''
import re
import sys


def get_values(fname, word):
	lines = []
	hba1c =  []
	line_number = 0
	found_at = -1

	with open(fname) as f:
		for line in f:
			line_number += 1
			if re.findall(word, line.lower()):
				hba1c.append(line)
				found_at = line_number

	return (hba1c, found_at)


def extract_percentage(hba1c):
	hba1c_values = []
	
	for line in hba1c:
		if re.findall(r'\d+\D*%', line):
			hba1c_values.append(re.findall(r'\d+\D*%', line))
	return hba1c_values


def create_i2b2(percentage, line_number, flag):
	
	'''
	percentage: holds the actual percentage value
	line_number: holds the line where the percentage was found
	flag: tells if the function was called for hba1c or hga1c

	'''
	line_number = str(line_number)+":0 "+str(line_number)+":0"
	final_string = ""
	if flag == "b":
		final_string += "c=\"hba1c\" "+str(line_number)+"||t=\"test\""
	elif flag == "g":
		final_string += "c=\"hga1c\" "+str(line_number)+"||t=\"test\""
	return final_string


def replace_num(file):
	
	'''
	This function takes in the file and checks for __num__ missing values, and then replaces
	with the correct number
	'''




def main():
	# Checking if file path is given or not
	if len(sys.argv) < 3:
		print "Usage: python ",sys.argv[0]," <path to txt>"
		sys.exit()

	fname = sys.argv[1]
	fname2 = sys.argv[2]
	print fname2

	# Searching for hba1c and hga1c in the file
	# line_number_b holds the location where the hba1c statement is found
	hba1c, line_number_b = get_values(fname, "hba1c")
	# print hba1c, line_number_b

	# line_number_g holds the location where the hga1c statement is found
	hga1c, line_number_g = get_values(fname, "hga1c")
	# print hga1c, line_number_g

	# Now getting the exact percentage value of Hb1AC
	if hba1c:
		hba1c_values = extract_percentage(hba1c)[0][0]
		print hba1c_values
		# Now converting to the i2b2 format
		i2b2_b = create_i2b2(hba1c_values, line_number_b, "b")
		print i2b2_b
		with open(fname2, "a") as f:
			f.write(i2b2_b)


	# Now getting the exact percentage value of Hg1AC
	if hga1c:
		hga1c_values = extract_percentage(hga1c)[0][0]
		print hga1c_values
		# Now converting to the i2b2 format
		i2b2_g = create_i2b2(hga1c_values, line_number_g, "g")	
		print i2b2_g
		with open(fname2, "a") as f:
			f.write("\n"+i2b2_g)

if __name__ == '__main__':
	main()
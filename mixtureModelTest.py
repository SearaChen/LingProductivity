import csv 
import re 
import sys 


def parseMorphemeFiles(filepath = ""):
	
	# creating feature set
	print("first pass")
	feature_set=set({})

	input_f = open(filepath, 'rb')
	f_output = open(resultFilePath , 'w', newline = '')
	tsv_output = csv.writer(f_output, delimiter='\t')

	for _ in range(2):
		next(input_f)
	for line in input_f:
		line = line.decode("UTF-8").lower()
		elements = line.strip().rstrip().split(" ")
		data = [e.strip().lower() for e in elements if e != '+' and not bool(re.search(r'[1-9]', e))]
		tsv_output.writerow(data)

	input_f.close()
	f_output.close()

	
if __name__ == "__main__":
	file = "./baysian_input.tsv"
	parseMorphemeFiles(file)
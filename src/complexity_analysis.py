
import sys 
import re


def segmentfile_analyze(filepath , write_to_filepath = None): 
	element_dic = {} # key: the construction   value: the times it appeared

	compounds_count = 0;
	with open(filepath, 'rb') as f:
		for _ in range(2):
			next(f)
		for line in f:
			compounds_count+=1
			line = line.decode("UTF-8").lower()
			elements = line.strip().rstrip().split(" ");
			for e in elements:
				if e == '+' or bool(re.search(r'[1-9]', e)):
					continue
				e = e.strip().rstrip()
				e=e.encode('ascii','replace')
				try : 
					element_dic[e]+=1
				except:
					element_dic[e]=1

	# count average length of construction
	# count total constructions 
	# count total construction types (unique)
	# --------------------------------- making calculations ------------------------------------
	x  = 0   #total_constructions_count
	c = len(element_dic.keys()) # unique construction types 
	total_construction_length =0
	
	for key in element_dic.keys():
		x += element_dic[key] 
		total_construction_length+=len(key.decode('ascii','replace'))
	
	average_construction_length=(float)(total_construction_length)/(c)
	average_number_constructions_in_compound = (float)(x)/compounds_count

	print (' -- FILE RESULT --')
	print ('unique construction types (c): '+ str(c))
	print ('total number of constructions: ' + str(x))
	print ('average construction length: ' + str(average_construction_length))
	print ('average number of construction per compound: ' + str(average_number_constructions_in_compound))


	if write_to_filepath != None:
		f= open(write_to_filepath, 'w')
		for key in element_dic.keys():
			f.write(key+ ' ' + str(element[key])+'\n')
		f.close()
	
	return (x, 
			c,
			average_construction_length,
			average_number_constructions_in_compound)

if __name__ == '__main__':
	alphas = [0.1,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,2.0]
	for a in alphas: 
		print ( "-------- " + str(a) + " -------------")
		filepath = "/Users/Seara/Desktop/COMP400Project/data/results/portugese_SBJV_segmented_"+str(a)+".txt"
		segmentfile_analyze(filepath)


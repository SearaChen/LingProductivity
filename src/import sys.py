#coding = português
import sys 
import re
from pathlib import Path


filepath = "/Users/Seara/Desktop/COMP400Project/data/results/portugese_SBJV_segmented_1.txt"
#filepath = "/Users/Seara/Desktop/COMP400Project/data/results/portugese_SBJV_segmented_0.5.txt"

#filepath = "../data/results/portugese_SBJV_segmented_0.5.txt"

count = 0

element_dic = {} # key: the construction   value: the times it appeared
with open(filepath, 'rb') as f:
	for _ in range(2):
		next(f)
	for line in f:
		line = line.decode("utf-8").lower()
		elements = line.strip().rstrip().split(" ");
		for e in elements:
			if e == '+' or bool(re.search(r'[1-9]', e)):
				continue
			e = e.strip().rstrip()
			e=e.encode('utf-8')
			try : 
				element_dic[e]+=1
			except:
				element_dic[e]=1
		
		print(e)
		count+=1
		if count == 10:
			element_dic
			sys.exit()


# count total constructions 
# count total construction types (unique)
total_constructions  = 0
total_contruction_types = 0
average_construction_length =0
for key in element_dic.keys():
	total_contruction_types+=1
	total_constructions += element_dic[key]
	average_construction_length+=len(key)

#average_construction_length=(float)(average_construction_length)/(total_contruction_types)

print ('unique construction types: '+ str(total_contruction_types))
print ('total number of contructions: ' + str(total_constructions))
print ('average construction length: ' + str(average_construction_length))
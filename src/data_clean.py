'''
Original Template built for portugese file
'''
import sys

def reach_requirement(analysis_list, necessary_attributes):
	# print (analysis_list)
	# print (necessary_attributes)
	# print(set(necessary_attributes).issubset(analysis_list))

	return set(necessary_attributes).issubset(analysis_list)


def clean_necessary_attributes(necessary_attributes):
	result=[]
	for x in list(necessary_attributes):
		result.append(x.lower())
	return set(result)


def main(attributes=["V", "3"], raw_filename="", cleaned_filename=""):
	necessary_attributes = clean_necessary_attributes(attributes)
	corpus_text_file = open(cleaned_filename, "wb")
	with open(raw_filename, 'rb') as f:
		for line in f:
			
			try:
				inf, word, analysis = line.split()
			except:
				continue

			analysis = analysis.decode("utf-8").lower()
			analysis_list = analysis.strip().rstrip().split(";")

			if reach_requirement(analysis_list,necessary_attributes):
				corpus_text_file.write(b"1 "+word + b" \n")

	corpus_text_file.close()


if __name__ == '__main__':
	main(attributes=["v","3","SG","PRS"],raw_filename="/Users/Seara/Desktop/COMP400Project/data/portugese_unimorph_data.txt",cleaned_filename="/Users/Seara/Desktop/COMP400Project/lol.txt");
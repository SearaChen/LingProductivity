
def main(segmentation_filename="", segments_count_filename=""):
	elements={}

	with open (segmentation_filename, 'rb') as f:
		for line in f: 
			items = line.split()[1:]

			for x in items:
				if x == '-' or x == '+':
					continue
				else:
					try:
						elements[x.lower()]+=1:
					except:
						elements[x.lower()] = 1

	f= open(segments_count_filename ,'w')
	for key, value in reverse(sorted(elements.iteritems(), key=lambda (k,v): (v,k))):
		f.write(key + " " + value)
	f.close()


if __name__ == '__main__' : 
	directory = "/Users/Seara/Desktop/COMP400Project/data/results/portugese_v-3-SG-IND-FUT_segmented.txt"
	main(segmentation_filename=directory,
		segmentation_filename = )
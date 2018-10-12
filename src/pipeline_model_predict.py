
"""
calling in order : data_clean.py , original_model_predict.py
"""

import original_model_predict
import data_clean

domain_dir = "/Users/Seara/Desktop/COMP400Project/"
language = "portugese"
attributes = ["SBJV"]


experiment_threshold = [0.01]
experiment_algorithm = ['recursive', 'viterbi']


raw_data_unimorph_filename = domain_dir+'data/'+language+'_unimorph_data.txt'
cleaned_data_filename = domain_dir + 'data/'+language+'_' + '-'.join(attributes) + '.txt'

data_clean.main(attributes=attributes,
				raw_filename=raw_data_unimorph_filename,
				cleaned_filename=cleaned_data_filename)

for x in experiment_algorithm: 
	for y in experiment_threshold:
		print ("here!!")
		segmentation_filename = domain_dir + 'data/results/'+language+'_' + '-'.join(attributes) + '_segmented_'+x+'_'+str(y)+'.txt'
		original_model_predict.predict(corpus_filename = cleaned_data_filename,
									   segmentation_filename = segmentation_filename,
									   finish_threshold = y,
									   algorithm = x
									)
		print("we are done!!")


# import original_model_predict
# import data_clean
# import sys
# sys.path.append('/Users/Seara/Desktop/COMP400Project/morfessor/morfessor')
# import baselineModifiedModel as bmm
# import morfessor


# def predict(corpus_filename="", segmentation_filename="", finish_threshold = 0.005, algorithm = 'recursive',corpusweight = 1):
# 	io = morfessor.MorfessorIO()
# 	train_data = list(io.read_corpus_file(corpus_filename))
# 	model = bmm.BaselineModel(corpusweight = corpusweight)
# 	model.load_data(train_data)
# 	model.train_batch(algorithm='recursive',finish_threshold=finish_threshold, max_epochs=None)
# 	segmentations = model.get_segmentations()
# 	io.write_segmentation_file(segmentation_filename, segmentations)



# domain_dir = "/Users/Seara/Desktop/COMP400Project/"
# language = "portugese"
# attributes = ["SBJV"]

# alphas = [1.0]


# raw_data_unimorph_filename = domain_dir+'data/'+language+'_unimorph_data.txt'
# cleaned_data_filename = domain_dir + 'data/'+language+'_' + '-'.join(attributes) + '.txt'

# data_clean.main(attributes=attributes,
# 				raw_filename=raw_data_unimorph_filename,
# 				cleaned_filename=cleaned_data_filename)

# for a in alphas : 
# 	segmentation_filename = domain_dir + 'data/results/'+language+'_' + '-'.join(attributes) + '_segmented_'+str(a)+'.txt'
# 	predict(corpus_filename = cleaned_data_filename,
# 			segmentation_filename = segmentation_filename,
# 			corpusweight= a 
# 			)
s ='a'
s.upper()
print(s == s.lower())
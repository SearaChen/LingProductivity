import morfessor

'''
Train batch has following parameters: 
algorithm='recursive'
algorithm_params=()
finish_threshold=0.005
max_epochs=None
'''
def predict(corpus_filename="", segmentation_filename="", finish_threshold = 0.005, algorithm = 'recursive'):
	io = morfessor.MorfessorIO()
	train_data = list(io.read_corpus_file(corpus_filename))
	model = morfessor.BaselineModel()
	model.load_data(train_data)
	model.train_batch(algorithm='recursive',finish_threshold=finish_threshold, max_epochs=None)
	segmentations = model.get_segmentations()
	io.write_segmentation_file(segmentation_filename, segmentations)
	

if __name__ == '__main__':
	print("hi")

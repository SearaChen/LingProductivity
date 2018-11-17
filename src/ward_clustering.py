# encoding=utf8
"""
using : ward hierchacal clustering  https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.cluster.hierarchy.ward.html
was weighted Levenshtein distance implemented with weighted_levenshtein.
And the comparison was by V-measure calculated with sklearn.metrics.v_measure_score./
"""
import sys
import re
from matplotlib import pyplot as plt
import  scipy.cluster.hierarchy as ch
import numpy as np
from sklearn.metrics.cluster import v_measure_score
from weighted_levenshtein import lev, osa, dam_lev
from scipy.spatial.distance import pdist
#from scipy.cluster import ward


"""
3. map retrieved cluster and graph  --- match
"""

def encodingDataSet(filepath=""):

	# creating feature set
	print("first pass")
	feature_set=set({})
	word_stem_dic = {}
	max_count =0
	with open(filepath, 'rb') as f:
		for _ in range(2):
			next(f)
		for line in f:
			line = line.decode("UTF-8").lower()
			elements = line.strip().rstrip().split(" ")
			count = 0
			for e in elements:
				if e == '+' or bool(re.search(r'[1-9]', e)):
					continue
				else:
					feature_set.add(e.strip().rstrip().lower())
					count +=1
			max_count = count if count > max_count else max_count

	feature_set = [x.encode('utf-8') for x in list(feature_set)]
	# print x.encode('utf-8') # if want to print
	
	print("Second pass")
	feature_code_dic = {} # key: word_seg  ; value : number code
	for index, item in enumerate(feature_set):
		feature_code_dic[item] = index

	X=[]
	original_data_set=[]
	with open(filepath, 'rb') as f:
		for _ in range(2):
			next(f)
		for line in f:
			encoded_data_entry = [None]*max_count
			original_data_entry = ""
			line = line.decode("UTF-8").lower()
			elements = line.strip().rstrip().split(" ");
			elements = [e for e in elements if e != '+' and not bool(re.search(r'[1-9]', e))]
			original_data_entry = ''.join(elements)
			encoded_data_entry = encodeSegmentsToNumbers(elements,feature_code_dic,encoded_data_entry)
			X.append(encoded_data_entry)
			original_data_set.append(original_data_entry.encode("utf-8"))
	return (original_data_set, X)

# encoding function from segments to number
def encodeSegmentsToNumbers(s,feature_code_dic,data_entry):
	"""
	input: 
	output: 
	"""
	for index, item in enumerate(s):

		item = item.encode("UTF-8")
		data_entry[index] = feature_code_dic[item]
	return data_entry


# distance function 
def distanceLev(s,t):

	# scoring system: 0 is match, 1 otherwise
	if not s.any(): return len(t)
	elif not t.any(): return len(s)

	s = [x for x in s if x!= None]
	t = [x for x in t if x!= None]

	v0 = [None] * (len(t) + 1)
	v1 = [None] * (len(t) + 1)
	for i in range(len(v0)):
		v0[i] = i
	for i in range(len(s)):
		v1[0] = i + 1
		for j in range(len(t)):
			cost = 0 if s[i] == t[j] else 1
			v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
		for j in range(len(v0)):
			v0[j] = v1[j]

	return v1[len(t)]

def testEncode(s):
	result=[]
	for letter in s:
		result.append(ord(letter))
	return result

def graph(Z):
	plt.figure()
	plt.title('Hierarchical Clustering Dendrogram (truncated)')
	plt.xlabel('sample index or (cluster size)')
	plt.ylabel('distance')
	ch.dendrogram(
	    Z,
	    truncate_mode='level',  # show only the last p merged clusters,  option: "lastp", "level"
	    p=2,  # show only the last p merged clusters
	    #leaf_rotation=90.,
	    leaf_font_size=12.,
	    show_contracted=True,  # to get a distribution impression in truncated branches
	)
	"""
	lastp : The last p non-singleton clusters formed in the linkage are the only non-leaf nodes in the linkage
	level : No more than p levels of the dendrogram tree are displayed. A “level” includes all nodes with p merges from the last merge
	"""
	ch.set_link_color_palette(['m', 'c', 'y', 'k'])
	#plt.show()
	plt.savefig("/Users/Seara/Desktop/COMP400Project/data/results/cluster/graph.png")
	#plt.close()

def fCluster(Z):
	"""
	Form flat clusters from the hierarchical clustering defined by the given linkage matrix
	https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html#scipy.cluster.hierarchy.fcluster
	- overall clustering algorithm, focus more on the global distance
	"""
	max_d = 50
	clusters = ch.fcluster(Z, max_d, criterion='distance')


def clustersToFile(cluster_dict, resultFileName = "", print_cluster_info = True):
	"""
	writing the cluster dictionary to a file for readability
	"""
	f = open(resultFileName,'wb')
	for index, key in enumerate(cluster_dict.keys()):
		titlestring = "------------------------ cluster #" + (str(index)) + ": -------------------------- \n" 
		f.write(bytes(titlestring,'utf-8'))
		for item in cluster_dict[key]:
			# if isinstance(item,bytes):
			# 	item = unicode(item, "utf-8")
			# 	f.write(item.encode("utf-8"))
			# elif isinstance(item, str):
			# 	item = unicode(item, "utf-8")
			# 	f.write(item.encode("utf-8"))
			# else:
			try:
				f.write(item)
			except:
				print (item)
				sys.exit()

			f.write(b'\n')
			if print_cluster_info:
				print("cluster #" + str(index) + ": " + str(len(cluster_dict[key])))
	f.close()




if __name__ == '__main__':
	filepath = "/Users/Seara/Desktop/COMP400Project/data/results/portugese_SBJV_segmented_1.0.txt"
	#filepath = "/Users/Seara/Desktop/COMP400Project/data/results/segmented_test.txt"
	print("Encoding dataset ...")
	original_data_set, X=encodingDataSet(filepath)

	print("Performing linkage ...")
	Z= ch.linkage(X,
			method='single',  # completeL 0.18 ; average : 0. 3575; minimum: 0.4570 ;
			metric=distanceLev, 
			optimal_ordering=False)

	graph(Z)

	# check cophenetic distance
	print ("Computing choph distance...")
	Y = pdist(X, distanceLev);
	c, coph_dists = ch.cophenet(Z, Y) # Cophenetic Correlation Coefficient  
	print(c)
	
	# retrieve clustering 
	cut_tree = ch.cut_tree(Z, n_clusters=5)
	"""
	height : array_like,The height at which to cut the tree. Only possible for ultrametric trees.
	n_clusters : array_like, optional : Number of clusters in the tree at the cut point.
	"""
	cut_tree = np.array(cut_tree).flatten()
	cluster_dict = {} # key: cluster code; value: original entry
	for i in range(cut_tree.shape[0]):
		try:
			cluster_dict[cut_tree[i]].append(original_data_set[i])
		except: 
			cluster_dict[cut_tree[i]]=[original_data_set[i]]

	# write to file
	cluster_result_filename = "/Users/Seara/Desktop/COMP400Project/data/results/cluster/cluster_portugese_SBJV_segmented_1.0.txt"
	clustersToFile(cluster_dict, resultFileName = cluster_result_filename)
	for index, key in enumerate(cluster_dict.keys()):
		print("cluster #" + str(index) + ": " + str(len(cluster_dict[key])))
		print (cluster_dict[key])


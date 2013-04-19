"""The affinity propagation clusterer object does a few things things:
	- sanitize the distance matrix.
	- convert the distance matrix into an affinity matrix.
	- perform affinity propagation clustering on the affinity matrix.
	- display the clustering."""

import csv
import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import math
from collections import defaultdict
from itertools import chain
import pylab as pl
from itertools import cycle

newline = '\n'

class AffinityPropagationClusterer(object):
	"""Initialize the distance matrix."""
	def __init__(self, filename_holder):
		self.fnh = filename_holder
		
		self.sanDistmat = []
	
	"""Fetch the distance matrix from file."""
	def fetch_distmat(self):
		self.in_file = open(self.fnh.get_fn_distmat(), 'rU')
		
		self.in_txt = csv.reader(self.in_file, delimiter = ' ')
	
	"""Sanitize the distance matrix."""
	def sanitize_distmat(self):
		for num, row in enumerate(self.in_txt, 1):
			if num == 1:
				pass
			else:
				sanitized_row = []
				for element in row:
					if element != '':
						sanitized_row.append(element)
				self.sanDistmat.append(sanitized_row)
	
	"""Get the sanitized distance matrix."""	
	def get_sanitized_distmat(self):
		return self.sanDistmat
	
	"""Write the sanitized distance matrix to a CSV file."""
	def write_sanDistmat(self):
		out_file = open(self.fnh.get_fn_sanDistmat(), 'w+')
		out_csv = csv.writer(out_file)
		for row in self.sanDistmat:
			out_csv.writerow(row)
		out_file.close()
		
	"""This method gets only the n by n set of values, excluding the names, and returns the list."""
	def get_sanDistmatArray(self):
		self.sanDistmatValues = []
		
		for row in self.sanDistmat:
			self.sanDistmatValues.append(row[1:])
		
		self.sanDistmatArray = np.array([row for row in self.sanDistmatValues]).astype(np.float)
		
		return self.sanDistmatArray
	
	"""This method gets only the IDs of the sequences in the distmat matrix."""
	def get_sanDistmatIDs(self):
		self.sanDistmatIDs = []
		
		for row in self.sanDistmat:
			self.sanDistmatIDs.append(row[0])
		
		return self.sanDistmatIDs
	
	"""This method computes the affinity matrix by applying a "kernel". Still don't know what a kernel is, but I know its form."""
	def compute_affmat(self):
	
		eulers = math.exp(1)
		self.distmat_stdev = np.std(self.get_sanDistmatArray())
		
		self.affmat = np.array([eulers ** (-row/self.distmat_stdev) for row in self.sanDistmatArray]).astype(np.float)
		self.set_fullaffmat()
	
	"""This method returns the affinity matrix array."""
	def get_affmat(self):
		return self.affmat
	
	"""Write affinity matrix to a CSV file."""
	def write_affmat(self):
		out_file = open(self.fnh.get_fn_affmat(), 'w+')
		out_csv = csv.writer(out_file)
		
		for row in self.get_fullaffmat():
			out_csv.writerow(row)
		
		out_file.close()
	
	"""Get and set the full affinity matrix.
	
	The affinity matrix, for computing purposes, is an array. This is not necessary for the full affinity matrix, as all we need is it tob e a list. Hence, in this method, we convert each row in the affmat into a list, add sanitized distmat IDs into the first position on each row, and append each row to the full list."""
	def set_fullaffmat(self):
		self.full_affmat = []
		
		for n, row in enumerate(self.get_affmat(), 0):
			listrow = list(row)
			listrow.insert(0, self.get_sanDistmatIDs()[n])
			self.full_affmat.append(listrow)

	def get_fullaffmat(self):
		return self.full_affmat
	
	"""Get the distance matrix standard deviation. Meant for interest."""
	def get_distmat_stdev(self):
		return self.distmat_stdev
		
	"""Compute affinity propagation."""
	def compute_affinity_propagation(self):
		self.af = AffinityPropagation(affinity = 'precomputed').fit(self.get_affmat())
		self.cluster_centers_indices = self.af.cluster_centers_indices_
		self.labels = self.af.labels_
		
		self.n_clusters = len(self.cluster_centers_indices)
		
		self.clusternames = defaultdict(list)
		
		for i, label in enumerate(self.labels):
			self.clusternames[label].append(self.sanDistmatIDs[i])

	
	"""Export report to your heart's content."""
	def write_txt_report(self):
		out_file = open(self.fnh.get_fn_report(), 'w+')
		
		for k, v in self.clusternames.items():
			print ("Cluster %s:" % str(k + 1))
			print ('\n')
			print (str(v))
			print ('\n')

			out_file.write("Cluster %s:" % str(k + 1))
			out_file.write('\n')
			out_file.write(str(v))
			out_file.write('\n')
			
		out_file.write('Estimated number of clusters: %d' % self.n_clusters)
		out_file.write(newline)
		out_file.write("Homogeneity: %0.3f" % metrics.homogeneity_score(self.sanDistmatIDs, self.labels))
		out_file.write(newline)
		out_file.write( "Completeness: %0.3f" % metrics.completeness_score(self.sanDistmatIDs, self.labels) )
		out_file.write(newline)
		out_file.write( "V-measure: %0.3f" % metrics.v_measure_score(self.sanDistmatIDs, self.labels))
		out_file.write(newline)
		out_file.write( "Adjusted Rand Index: %0.3f" % \
			metrics.adjusted_rand_score(self.sanDistmatIDs, self.labels))
		out_file.write(newline)
		out_file.write("Adjusted Mutual Information: %0.3f" %
			  metrics.adjusted_mutual_info_score(self.sanDistmatIDs, self.labels))
		out_file.write(newline)
		out_file.write("Silhouette Coefficient: %0.3f" %
			  metrics.silhouette_score(self.affmat, self.labels, metric='sqeuclidean'))
		
		out_file.close()
	
	
	"""Plot clusters."""
	def plot_clusters(self):
		pl.close('all')
		pl.figure(1)
		pl.clf()

		colors = cycle('bgrcmyk')
		for k, col in zip(range(self.n_clusters), colors):
			class_members = self.labels == k
			cluster_center = self.affmat[self.cluster_centers_indices[k]]
			pl.plot(self.affmat[class_members, 0], self.affmat[class_members, 1], col + '.')
			pl.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
					markeredgecolor='k', markersize=10)
			for x in self.affmat[class_members]:
				pl.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

		pl.title('Protein: %s' % self.fnh.get_segment())
		pl.suptitle('Estimated number of clusters: %d' % self.n_clusters)
		pl.show()
print __doc__

import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import csv
import math

segment = 'HA'

##############################################################################
# Open Data
f = open('sequences-distmat.csv', 'rU')
csvreader = csv.reader(f)

sequence_names = []
distance_matrix = []
full_data = []

for row in csvreader:
# 	print row
	
	sequence_names.append(row[0])
	distance_matrix.append(row[1:])
	full_data.append(row)

f.close()

print distance_matrix

distmat = np.array([row for row in distance_matrix]).astype(np.float)

# print distmat

distmat_sd = np.std(distmat)
print "Distmat standard deviation is %s" %distmat_sd

# affinity_matrix = np.array([1 - row for row in distmat]).astype(np.float)
affinity_matrix = np.array([2.73 ** (-row/distmat_sd) for row in distmat]).astype(np.float)

full_matrix = zip(sequence_names, affinity_matrix)

# print affinity_matrix, sequence_names




##############################################################################
# Compute Affinity Propagation
af = AffinityPropagation(affinity='precomputed').fit(affinity_matrix)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

# print labels

n_clusters_ = len(cluster_centers_indices)

from collections import defaultdict
clusternames = defaultdict(list)

for i, label in enumerate(labels):
	clusternames[label].append(sequence_names[i])
	
print "Clusters:"
#Write clusters to a text file for storage.
with open('%s-sequence-clusters.txt' % segment, 'w+') as f:
	for k, v in clusternames.items():
		f.write(str(k))
		f.write('\n')
		f.write(str(v))
		f.write('\n')
		print k, v

print 'Estimated number of clusters: %d' % n_clusters_
print "Homogeneity: %0.3f" % metrics.homogeneity_score(sequence_names, labels)
print "Completeness: %0.3f" % metrics.completeness_score(sequence_names, labels)
print "V-measure: %0.3f" % metrics.v_measure_score(sequence_names, labels)
print "Adjusted Rand Index: %0.3f" % \
    metrics.adjusted_rand_score(sequence_names, labels)
print("Adjusted Mutual Information: %0.3f" %
      metrics.adjusted_mutual_info_score(sequence_names, labels))
print("Silhouette Coefficient: %0.3f" %
      metrics.silhouette_score(affinity_matrix, labels, metric='sqeuclidean'))

##############################################################################
# Plot result
import pylab as pl
from itertools import cycle

pl.close('all')
pl.figure(1)
pl.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = affinity_matrix[cluster_centers_indices[k]]
    pl.plot(affinity_matrix[class_members, 0], affinity_matrix[class_members, 1], col + '.')
    pl.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=10)
    for x in affinity_matrix[class_members]:
        pl.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

pl.title('Protein: %s' % segment)
pl.suptitle('Estimated number of clusters: %d' % n_clusters_)
pl.show()
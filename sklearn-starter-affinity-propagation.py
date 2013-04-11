print __doc__

import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import csv

##############################################################################
# Generate sample data
# centers = [[1, 1], [-1, -1], [1, -1]]
# X, sequence_names = make_blobs(n_samples=60, centers=centers, cluster_std=0.5,
#                             random_state=0)
# 
# print X, sequence_names

# Open Data
f = open('ha-sequences-sample-distmat2.csv', 'rU')
csvreader = csv.reader(f)

sequence_names = []
distance_matrix = []
full_data = []

for row in csvreader:
	print row
	
	sequence_names.append(row[0])
	distance_matrix.append(row[1:])
	full_data.append(row)

f.close()

distmat = np.array([row for row in distance_matrix]).astype(np.float)

# print distmat

affinity_matrix = np.array([1 - row for row in distmat]).astype(np.float)

print affinity_matrix, sequence_names




##############################################################################
# Compute Affinity Propagation
af = AffinityPropagation(affinity='precomputed').fit(affinity_matrix)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

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
            markeredgecolor='k', markersize=14)
    for x in affinity_matrix[class_members]:
        pl.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

pl.title('Estimated number of clusters: %d' % n_clusters_)
pl.show()
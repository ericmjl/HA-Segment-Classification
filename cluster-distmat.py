print __doc__

# Author: Eric Ma ericmajinglong@gmail.com
# License: Unknown
# Modified from sample code provided by scikit-learn.

import datetime

import numpy as np
import pylab as pl
from matplotlib import finance
from matplotlib.collections import LineCollection
import csv

from sklearn import cluster, covariance, manifold

###############################################################################
"""Import CSV file containing the distance matrix. The CSV file is currently structured as such: 
	- 1st column contains sequence name
	- 2nd to 71st columns contain sequence distance to every other sequence.
	- There are 70 rows in total."""

f = open('ha-sequences-sample-distmat.csv', 'rU')
csvreader = csv.reader(f)

sequence_names = []
distance_matrix = []

for row in csvreader:
	sequence_names.append(row[0])
	distance_matrix.append(row[1:])


f.close()

# print sequence_names

# for row in sequence_names:
# 	print row

# print distance_matrix

# for row in distance_matrix:
# 	print row


# symbol_dict = {
#     'TOT': 'Total',
#     'XOM': 'Exxon',
#     'CVX': 'Chevron',
#     'COP': 'ConocoPhillips',
#     'VLO': 'Valero Energy',
#     'MSFT': 'Microsoft',
#     'IBM': 'IBM',
#     'TWX': 'Time Warner',
#     'CMCSA': 'Comcast',
#     'CVC': 'Cablevision',
#     'YHOO': 'Yahoo',
#     'DELL': 'Dell',
#     'HPQ': 'HP',
#     'AMZN': 'Amazon',
#     'TM': 'Toyota',
#     'CAJ': 'Canon',
#     'MTU': 'Mitsubishi',
#     'SNE': 'Sony',
#     'F': 'Ford',
#     'HMC': 'Honda',
#     'NAV': 'Navistar',
#     'NOC': 'Northrop Grumman',
#     'BA': 'Boeing',
#     'KO': 'Coca Cola',
#     'MMM': '3M',
#     'MCD': 'Mc Donalds',
#     'PEP': 'Pepsi',
#     'KFT': 'Kraft Foods',
#     'K': 'Kellogg',
#     'UN': 'Unilever',
#     'MAR': 'Marriott',
#     'PG': 'Procter Gamble',
#     'CL': 'Colgate-Palmolive',
#     'NWS': 'News Corp',
#     'GE': 'General Electrics',
#     'WFC': 'Wells Fargo',
#     'JPM': 'JPMorgan Chase',
#     'AIG': 'AIG',
#     'AXP': 'American express',
#     'BAC': 'Bank of America',
#     'GS': 'Goldman Sachs',
#     'AAPL': 'Apple',
#     'SAP': 'SAP',
#     'CSCO': 'Cisco',
#     'TXN': 'Texas instruments',
#     'XRX': 'Xerox',
#     'LMT': 'Lookheed Martin',
#     'WMT': 'Wal-Mart',
#     'WAG': 'Walgreen',
#     'HD': 'Home Depot',
#     'GSK': 'GlaxoSmithKline',
#     'PFE': 'Pfizer',
#     'SNY': 'Sanofi-Aventis',
#     'NVS': 'Novartis',
#     'KMB': 'Kimberly-Clark',
#     'R': 'Ryder',
#     'GD': 'General Dynamics',
#     'RTN': 'Raytheon',
#     'CVS': 'CVS',
#     'CAT': 'Caterpillar',
#     'DD': 'DuPont de Nemours'}
# 
# symbols, names = np.array(symbol_dict.items()).T
# 
# quotes = [finance.quotes_historical_yahoo(symbol, d1, d2, asobject=True)
#           for symbol in symbols]
# 
# open = np.array([q.open for q in quotes]).astype(np.float)
# close = np.array([q.close for q in quotes]).astype(np.float)
# 
# # The daily variations of the quotes are what carry most information
# variation = close - open
# print variation

"""The distance matrix is the most important information."""

edge_model = covariance.GraphLassoCV()

distmat = np.array([row for row in distance_matrix]).astype(np.float)
print distmat

names = np.array([row for row in sequence_names])
X = distmat.copy().T
X /= X.std(axis=0)

edge_model.fit(X)

# 
# ###############################################################################
# # Learn a graphical structure from the correlations
# edge_model = covariance.GraphLassoCV()
# 
# # standardize the time series: using correlations rather than covariance
# # is more efficient for structure recovery
# X = variation.copy().T
# X /= X.std(axis=0)
# print X.shape
# print X
# edge_model.fit(X)
# 
###############################################################################
# Cluster using affinity propagation

_, sequence_names = cluster.affinity_propagation(edge_model.covariance_)
n_labels = sequence_names.max()

for i in range(n_labels + 1):
    print 'Cluster %i: %s' % ((i + 1), ', '.join(names[sequence_names == i]))

###############################################################################
# Find a low-dimension embedding for visualization: find the best position of
# the nodes (the stocks) on a 2D plane

# We use a dense eigen_solver to achieve reproducibility (arpack is
# initiated with random vectors that we don't control). In addition, we
# use a large number of neighbors to capture the large-scale structure.
node_position_model = manifold.LocallyLinearEmbedding(
    n_components=2, eigen_solver='dense', n_neighbors=6)

embedding = node_position_model.fit_transform(X.T).T

###############################################################################
# Visualization
pl.figure(1, facecolor='w', figsize=(10, 8))
pl.clf()
ax = pl.axes([0., 0., 1., 1.])
pl.axis('off')

# Display a graph of the partial correlations
partial_correlations = edge_model.precision_.copy()
d = 1 / np.sqrt(np.diag(partial_correlations))
partial_correlations *= d
partial_correlations *= d[:, np.newaxis]
non_zero = (np.abs(np.triu(partial_correlations, k=1)) > 0.02)

# Plot the nodes using the coordinates of our embedding
pl.scatter(embedding[0], embedding[1], s=100 * d ** 2, c=sequence_names,
           cmap=pl.cm.spectral)

# Plot the edges
start_idx, end_idx = np.where(non_zero)
#a sequence of (*line0*, *line1*, *line2*), where::
#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments = [[embedding[:, start], embedding[:, stop]]
            for start, stop in zip(start_idx, end_idx)]
values = np.abs(partial_correlations[non_zero])
lc = LineCollection(segments,
                    zorder=0, cmap=pl.cm.hot_r,
                    norm=pl.Normalize(0, .7 * values.max()))
lc.set_array(values)
lc.set_linewidths(15 * values)
ax.add_collection(lc)

# Add a label to each node. The challenge here is that we want to
# position the labels to avoid overlap with other labels
for index, (name, label, (x, y)) in enumerate(
        zip(names, sequence_names, embedding.T)):

    dx = x - embedding[0]
    dx[index] = 1
    dy = y - embedding[1]
    dy[index] = 1
    this_dx = dx[np.argmin(np.abs(dy))]
    this_dy = dy[np.argmin(np.abs(dx))]
    if this_dx > 0:
        horizontalalignment = 'left'
        x = x + .002
    else:
        horizontalalignment = 'right'
        x = x - .002
    if this_dy > 0:
        verticalalignment = 'bottom'
        y = y + .002
    else:
        verticalalignment = 'top'
        y = y - .002
    pl.text(x, y, name, size=10,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            bbox=dict(facecolor='w',
                      edgecolor=pl.cm.spectral(label / float(n_labels)),
                      alpha=.6))

pl.xlim(embedding[0].min() - .15 * embedding[0].ptp(),
        embedding[0].max() + .10 * embedding[0].ptp(),)
pl.ylim(embedding[1].min() - .03 * embedding[1].ptp(),
        embedding[1].max() + .03 * embedding[1].ptp())

pl.show()

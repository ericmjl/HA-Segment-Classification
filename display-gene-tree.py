from Bio import Phylo

import networkx, pylab

tree = Phylo.read('m-phylogeny.xml', 'phyloxml')
tree.ladderize()
Phylo.draw(tree)
# net = Phylo.to_networkx(tree)
# networkx.draw(net)
# pylab.show()
# a = [('fontsize', 25)]
# Phylo.draw_graphviz(tree, prog='twopi', args=a,node_size=0)
# pylab.show()
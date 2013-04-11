from Bio import Phylo

m_sequence_tree = Phylo.read("ha-sequences-sample-tree.phy_phyml_tree.txt", "newick")
Phylo.draw_ascii(m_sequence_tree)

from Bio.Phylo import PhyloXML

# Promote the basic tree to PhyloXML
m_phy = m_sequence_tree.as_phyloxml()

Phylo.write(m_phy, 'm-phylogeny.xml', 'phyloxml')
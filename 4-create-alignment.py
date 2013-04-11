from Bio import Phylo
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo import PhyloXML
import pylab
import matplotlib

cmdline = ClustalOmegaCommandline(infile="ha-sequences-sample.fasta", outfile="ha-sequences-sample-tree.aln", distmat_full=True, verbose=True, auto=False, force=True, distmat_out="ha-sequences-sample-distmat.txt")
print cmdline()

align = AlignIO.read('ha-sequences-sample-tree.aln', 'fasta')
print align


# cmdline = PhymlCommandline(input='m-sequences-aligned.phy', datatype='', model='WAG', alpha='e', bootstrap=100)
# out_log, error_log = cmdline()

# m_sequence_tree = Phylo.read('clustalw2_phylogeny-E20130409-200155-0136-79039013-pg.ph', 'phylip')
# m_sequence_tree.ladderize()
# Phylo.draw(m_sequence_tree)
# pylab.show()

# m_phy = m_sequence_tree.as_phyloxml()
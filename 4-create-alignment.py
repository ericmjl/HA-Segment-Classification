from Bio import Phylo
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo import PhyloXML
import pylab
import matplotlib

cmdline = ClustalOmegaCommandline(infile="sequences.fasta", outfile="sequences-tree.aln", distmat_full=True, verbose=True, auto=False, force=True, distmat_out="sequences-distmat.txt")
print cmdline()

align = AlignIO.read('sequences-tree.aln', 'fasta')
print align
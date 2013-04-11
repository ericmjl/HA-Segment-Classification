from Bio import AlignIO

AlignIO.convert("ha-sequences-sample-tree.aln", 'fasta', 'ha-sequences-sample-tree.phy', "phylip-relaxed")

from Bio.Phylo.Applications import PhymlCommandline

cmdline = PhymlCommandline(input='ha-sequences-sample-tree.phy', datatype='aa', model='WAG', alpha='e', bootstrap=100)

out_log, err_log = cmdline()
"""The sequence aligner object can do two things:
	- generate the FASTA file from the sampled list.
	- perform the multiple sequence alignment.
	
	As usual, the FilenameHolder object always is passed in, so that the full range of 
	filenames is available for the object."""
	
import csv
from Bio.Seq import Seq
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO

class SequenceAligner(object):
	def __init__(self, filename_holder):
		self.sequences = []
		
		self.fnh = filename_holder
	
	"""Fetch the sequences from the sampled CSV file, store them as a list of dictionaries"""
	def fetch_sequences(self):
		in_file = open(self.fnh.get_fn_subset(), 'rU')
		
		sequences = csv.DictReader(in_file)
		
		for row in sequences:
			self.sequences.append(row)
		
		in_file.close()
		
	"""Write the sequences from the list of dictionaries into a FASTA file."""
	def write_sequences_fasta(self):
		out_file = open(self.fnh.get_fn_fasta(), 'w+')
		
		for row in self.sequences:
			sequence = Seq(row['sequence'], generic_protein)
			id = row['id_long']
			name = row['strain_name']
			description = row['subtype']
			
			record = SeqRecord(sequence, id, name, description)
			
			SeqIO.write(record, out_file, 'fasta')
			
		out_file.close()
	
	"""Perform multiple sequence alignment on the sequences."""
	def perform_alignment(self):
		inputFileName = self.fnh.get_fn_fasta()
		outputFileName = self.fnh.get_fn_aln()
		distmatFileName = self.fnh.get_fn_distmat()
		
		cmdline = ClustalOmegaCommandline(infile=inputFileName, outfile=outputFileName, distmat_full=True, verbose=True, auto=False, force=True, distmat_out=distmatFileName)
		
		cmdline()
		
	def print_alignment(self):
		align = AlignIO.read(self.fnh.get_fn_aln(), 'fasta')
		print align

	def start_standard_workflow(self):
		self.fetch_sequences()
		self.write_sequences_fasta()
		self.perform_alignment()
		self.print_alignment()
import csv
from Bio.Seq import Seq
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
"""This script opens up the CSV file containing the HA sequences, and parses it to generate a FASTA file. The general steps are as follows:
	- Create Seq objects for each strain's DNA sequence
	- Create Seq objects for each strain's Protein sequence
	- Create SeqRecord (DNA and Protein separately) object for each strain
	- Output a combined FASTA file for inputting into clustalo for generating an alignment."""
	
"""Open the HA sequence CSV file as a list of dictionaries."""
ha_sequences = []

with open ('sequences-sample.csv', 'rU') as f:
	sequences = csv.DictReader(f)
	
	for row in sequences:
		ha_sequences.append(row)

"""Parse ha_sequences (list of dictionaries) to create DNA Seq objects for each row, and add them to a SeqRecord object."""


with open('sequences.fasta', 'w') as g:
	for row in ha_sequences:
# 		print row
	# 	seq = row['sequence']
		sequence = Seq(row['sequence'], generic_protein)
		id = row['subtype'] + row['accession']
		name = row['strain_name']
		description = row['subtype']
	
		record = SeqRecord(sequence, id, name, description)
	
# 		print record.format('fasta')
		
		SeqIO.write(record, g, "fasta")
		

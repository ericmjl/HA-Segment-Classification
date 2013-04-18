from Bio import SeqIO
from FilenameHolder import *
import csv

"""Here, I introduce a sequence parser object. This object is an abstraction that allows me to store information and read/write into CSV and TXT files.

Open up the sequences and store them in memory as a dictionary. The structure of the dictionary is as follows:
    { 
        'id'         :record.id
        'sequence'   :record.seq
        'translation':record.seq.translate()"""

class SequenceParser(object):

	"""Initialize the SequenceParser with three strings.
		- 'segment' is the segment name that we are going to parse - HA, NA, etc.
		- 'species' is the species name of the sequences - Human, Pig, etc.
		- 'strain' is the influenza strain name - A, B, or C."""
	def __init__(self, filename_holder):
		
		self.fnh = filename_holder
		
# 		self.segment = segment
# 		self.species = species
# 		self.strain = strain
# 		
# 		self.filename_sequences = ''
# 		self.filename_table_txt = ''
# 		self.filename_table_csv = ''
# 		self.filename_compiled = ''
# 		self.filenames = self.set_filenames_list()
		
		self.seq_db = []
		
		self.data_db = []
		
		self.compiled_db = []
		
# 	"""Generate the filenames. These are merely strings."""	
# 	def set_filenames(self):
# 	
# 		self.filename_sequences = 'Influenza A Human Strains %s Protein Sequences.gb' % self.segment
# 		self.filename_table_txt = 'Influenza A Human Strains %s Protein Sequences.txt' % self.segment
# 		self.filename_table_csv = 'Influenza A Human Strains %s Protein Sequences.csv' % self.segment
# 		self.filename_compiled = 'Influenza A Human Strains %s Compiled Sequences.csv' % self.segment
# 		
# 		self.set_filenames_list()
# 		
# 	def set_filenames_list(self):
# 		self.filenames = [self.filename_sequences, self.filename_table_txt, self.filename_table_csv, self.filename_compiled]
# 	
# 	"""Get the filename strings."""
# 	def get_filename(self, type):
# 	
# 		if type == 'sequences':
# 			return self.filename_sequences
# 			
# 		if type == 'table txt':
# 			return self.filename_table_txt
# 		
# 		if type == 'table csv':
# 			return self.filename_table_csv
# 		
# 		if type == 'compiled':
# 			return self.filename_compiled
# 		
# 		elif type == 'all':
# 			return self.filenames
# 		

	"""Get sequences from the genbank file."""
	def get_sequences(self):
	
		sequences = open(self.fnh.get_fn_sequences(), 'rU')
		
		for record in SeqIO.parse(sequences, 'genbank'):
			sequence = {}
			sequence['id'] = record.id
			sequence['sequence'] = record.seq
			self.seq_db.append(sequence)
		
		sequences.close()
	
	"""Print sequences that were read from the genbank file and stored in the seq_db 
	list, for diagnostic purposes."""
	def print_seq_db(self):
	
		for row in self.seq_db:
			print row
	
	"""Convert the data table - it is usually provided in a TXT file format, but this 
	code will convert it into a CSV file."""
	def convert_data_table(self):
	
		in_file = open(self.fnh.get_fn_table_txt(), 'rU')
		in_txt = csv.reader(in_file, delimiter = "	")
		
		out_file = open(self.fnh.get_fn_table_csv(), 'w+')
		out_csv = csv.writer(out_file)
		
		for row in in_txt:
			out_csv.writerow(row)
		
		in_file.close()
		out_file.close()
	
	"""Open up the data table (just converted above) that houses the strain name, 
	subtype, and other information. Read all the information as variables."""
	def get_data_table(self):
	
		in_file = open(self.fnh.get_fn_table_csv(), 'rU')
		data = csv.DictReader(in_file)
		
		for row in data:
			data = {}
			
			accession = row['Sequence Accession'].replace('*','')
			strain_name = row['Strain Name']
			subtype = row['Subtype']
			country = row['Country']
			state_province = row['State/Province']
			season = row['Flu Season']
			date_created = row['Creation Date']
			id = str(accession) + "|" + str(strain_name)

			data['accession'] = accession
			data['strain_name'] = strain_name
			data['subtype'] = subtype
			data['country'] = country
			data['state_province'] = state_province
			data['flu_season'] = season
			data['creation_date'] = date_created
			data['id'] = id
	
			self.data_db.append(data)
		
		in_file.close()
		
	def print_data_db(self):
		for row in self.data_db:
			print row
	
	"""Compare the information in seq_db to data_db. If the 'id' in the data_db is 
	identical to the id in seq_db, then add the subtype, and all corresponding 
	information, to compiled_db."""
	def compare_data_table(self):
	
		for sequence in self.seq_db:
			for data in self.data_db:
				if sequence['id'] == data['id']:
					compiled = {}
					compiled['id'] = data['id']
					compiled['subtype'] = data['subtype']
					compiled['accession'] = data['accession']
					compiled['strain_name'] = data['strain_name']
					compiled['country'] = data['country']
					compiled['state_province'] = data['state_province']
					compiled['flu_season'] = data['flu_season']
					compiled['creation_date'] = data['creation_date']
					compiled['sequence'] = sequence['sequence']
					
					self.compiled_db.append(compiled)
	
	"""Write compiled data as a CSV file."""				
	def write_compiled_table(self):
		fieldnames = ['id', 'subtype', 'accession', 'sequence', 'strain_name', 'country', 'state_province', 'flu_season', 'creation_date']
		out_file = open(self.fnh.get_fn_compiled(), 'w+')
		dictwriter = csv.DictWriter(out_file, delimiter = ',', fieldnames = fieldnames)
		dictwriter.writerow(dict((fn, fn) for fn in fieldnames))
		for row in self.compiled_db:
			dictwriter.writerow(row)
		out_file.close()
	
	"""This is the standard workflow up till the sampling of sequences."""
	def start_standard_workflow(self):
# 		self.set_filenames()
		self.get_sequences()
		self.print_seq_db()
		self.convert_data_table()
		self.get_data_table()
		self.print_data_db()
		self.compare_data_table()
		self.write_compiled_table()
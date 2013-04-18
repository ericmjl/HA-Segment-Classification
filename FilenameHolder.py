class FilenameHolder(object):
	def __init__(self, segment, species, strain):
		self.segment = segment
		self.species = species
		self.strain = strain
		
		fn_sequences = ''
		fn_table_txt = ''
		fn_table_csv = ''
		fn_compiled = ''
		fns = []
	"""Get and set segment."""	
	def get_segment(self):
		return self.segment
		
	def set_segment(self, segment):
		self.segment = segment
	
	"""Get and set species."""
	def get_species(self):
		return self.species
		
	def set_species(self, species):
		self.species = species
	
	"""Get and set strain."""
	def get_strain(self):
		return self.strain
		
	def set_strain(self, strain):
		self.strain = strain
	
	"""Get and set fn_sequences."""
	def set_fn_sequences(self):
		self.fn_sequences = 'Influenza A Human Strains %s Protein Sequences.gb' % self.segment
		
	def get_fn_sequences(self):
		return self.fn_sequences
		
	"""Get and set fn_table_txt."""
	def set_fn_table_txt(self):
		self.fn_table_txt = 'Influenza A Human Strains %s Protein Sequences.txt' % self.segment
	
	def get_fn_table_txt(self):
		return self.fn_table_txt
	
	"""Get and set fn_table_csv."""
	def set_fn_table_csv(self):
		self.fn_table_csv = 'Influenza A Human Strains %s Protein Sequences.csv' % self.segment
	
	def get_fn_table_csv(self):
		return self.fn_table_csv
	
	"""Get and set fn_compiled."""
	def set_fn_compiled(self):
		self.fn_compiled = 'Influenza A Human Strains %s Compiled Sequences.csv' % self.segment
		
	def get_fn_compiled(self):
		return self.fn_compiled
		
	def name_all_files(self):
		self.set_fn_sequences()
		self.set_fn_table_txt()
		self.set_fn_table_csv()
		self.set_fn_compiled()
		
		return self.fn_sequences, self.fn_table_txt, self.fn_table_csv, self.fn_compiled
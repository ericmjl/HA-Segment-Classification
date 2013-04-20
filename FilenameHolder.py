class FilenameHolder(object):
	def __init__(self, segment, species, strain):
		self.segment = segment
		self.species = species
		self.strain = strain
		
		self.parameters = (self.strain, self.species, self.segment)
		
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
		self.fn_sequences = 'Influenza %s %s Strains %s Protein Sequences.gb' % self.parameters
		
	def get_fn_sequences(self):
		return self.fn_sequences
		
	"""Get and set fn_table_txt."""
	def set_fn_table_txt(self):
		self.fn_table_txt = 'Influenza %s %s Strains %s Protein Sequences.txt' % self.parameters
	
	def get_fn_table_txt(self):
		return self.fn_table_txt
	
	"""Get and set fn_table_csv."""
	def set_fn_table_csv(self):
		self.fn_table_csv = 'Influenza %s %s Strains %s Protein Sequences.csv' % self.parameters
	
	def get_fn_table_csv(self):
		return self.fn_table_csv
	
	"""Get and set fn_compiled."""
	def set_fn_compiled(self):
		self.fn_compiled = 'Influenza %s %s Strains %s Compiled Sequences.csv' % self.parameters
		
	def get_fn_compiled(self):
		return self.fn_compiled
		
	"""Get and set fn_subset."""
	def set_fn_subset(self):
		self.fn_subset = 'Influenza %s %s Strains %s Sampled Sequences.csv' % self.parameters
		
	def get_fn_subset(self):
		return self.fn_subset
		
	"""Get and set fn_fasta."""
	def set_fn_fasta(self):
		self.fn_fasta = 'Influenza %s %s Strains %s Pre-Alignment Sequences.fasta' % self.parameters
	
	def get_fn_fasta(self):
		return self.fn_fasta
		
	"""Get and set fn_aln."""
	def set_fn_aln(self):
		self.fn_aln = 'Influenza %s %s Strains %s Alignment.aln' % self.parameters
		
	def get_fn_aln(self):
		return self.fn_aln
		
	"""Get and set fn_distmat."""
	def set_fn_distmat(self):
		self.fn_distmat = 'Influenza %s %s Strains %s Distmat.txt' % self.parameters
		
	def get_fn_distmat(self):
		return self.fn_distmat
		
	"""Get and set fn_sanDistmat."""
	def set_fn_sanDistmat(self):
		self.fn_sanDistmat = 'Influenza %s %s Strains %s Sanitized Distmat.csv' % self.parameters
		
	def get_fn_sanDistmat(self):
		return self.fn_sanDistmat
		
	"""Get and set fn_affmat."""
	def set_fn_affmat(self):
		self.fn_affmat = 'Influenza %s %s Strains %s Affinity Matrix.csv' % self.parameters
		
	def get_fn_affmat(self):
		return self.fn_affmat
		
	"""Get and set fn_report."""
	def set_fn_report(self):
		self.fn_report = 'Influenza %s %s Strains %s Clustering Report.txt' % self.parameters
		
	def get_fn_report(self):
		return self.fn_report
		
	"""Get and set fn_fig."""
	def set_fn_fig(self):
		self.fn_fig = 'Influenza %s %s Strains %s Clustering Report.png' % self.parameters
		
	def get_fn_fig(self):
		return self.fn_fig
		
	def name_all_files(self):
		self.set_fn_sequences()
		self.set_fn_table_txt()
		self.set_fn_table_csv()
		self.set_fn_compiled()
		self.set_fn_subset()
		self.set_fn_fasta()
		self.set_fn_aln()
		self.set_fn_distmat()
		self.set_fn_sanDistmat()
		self.set_fn_affmat()
		self.set_fn_report()
		self.set_fn_fig()
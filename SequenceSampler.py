"""This is the "sampler" class. A "sampler" object is contains methods to randomly sample through all sequences such that analysis is only performed on a subset of samples."""

import csv
import random
from FilenameHolder import *

class SequenceSampler(object):
	
	"""Initialize the object."""
	def __init__(self, filename_holder):
		self.num_samples = ''
		self.records_list = []
		self.subset = []
		
		self.fieldnames = []
		
		self.fnh = filename_holder
	
	"""Open the file of sequences and read them into memory."""
	def fetch_sequences(self):
		in_file = open(self.fnh.get_fn_compiled(), 'rU')
		
		records = csv.DictReader(in_file)
		
		for n, row in enumerate(records):
			if n == 0:
				self.fieldnames = row.keys()
			self.records_list.append(row)
		
		in_file.close()
		
	"""Get records_list."""
	def get_records_list(self):
		return self.records_list
		
	"""Generate records_list."""
	def generate_records_list(self):
		for row in self.records_list:
			yield row
	
	"""Shuffle the records. Just coz we can."""
	def shuffle_records(self):
		random.shuffle(self.records_list)
		
	"""Extract a subset of n or less records."""
	def extract_subset(self, n):		
		if len(self.records_list) >= n:
			self.num_samples = n
			
		elif len(self.records_list) < n:
			self.num_samples = len(self.records_list)
		
		self.subset = random.sample(self.records_list, self.num_samples)
	
	"""Get the entire subset list."""
	def get_subset(self):
		return self.subset
	
	"""Write the entire subset list to a CSV file."""
	def write_subset(self):
		out_file = open(self.fnh.get_fn_subset(), 'w+')
		
		csvwriter = csv.DictWriter(out_file, delimiter = ',', fieldnames = self.fieldnames)
		csvwriter.writerow(dict((fn,fn) for fn in self.fieldnames))
		for row in self.subset:
			csvwriter.writerow(row)
		
		out_file.close()
	
	"""This is the most common workflow:
		- read sequences from the CSV file of all sequences.
		- shuffle records to randomize their order.
		- extract a subset of n samples
		- write the subset to a 'sampled' CSV file."""
	def start_standard_workflow(self, n):
		self.fetch_sequences()
		self.shuffle_records()
		self.extract_subset(n)
		self.write_subset()
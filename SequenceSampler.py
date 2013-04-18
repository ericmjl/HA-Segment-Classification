"""This is the "sampler" class. A "sampler" object is contains methods to randomly sample through all sequences such that analysis is only performed on a subset of samples."""

import csv
import random
from FilenameHolder import *

class SequenceSampler(object):
	
	"""Initialize the object."""
	def __init__(self, fnh):
		self.num_samples = ''
		self.records_list = []
	
	def read_sequences(self, file):
	
	def extract_subset(self, num_samples):
		self.num_samples = num_samples
		
		
		
		
		
		
		
with open('sequences.csv', 'rU') as f:
	records = csv.DictReader(f)
	
	for row in records:
		records_list.append(row)
	
	random.shuffle(records_list) #just coz I can lol
	
	"""Extract 200 records max."""
	max_records = 200
	if len(records_list) >= max_records:
		num_samples = max_records
	
	if len(records_list) < max_records:
		num_samples = len(records_list)
	
	sample = random.sample(records_list, num_samples)
	
	
with open('sequences-sample.csv', 'w') as g:
	fieldnames = ['id', 'subtype', 'accession', 'strain_name', 'sequence']
	
	csvwriter = csv.DictWriter(g, delimiter = ',', fieldnames = fieldnames)
	csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
	for row in sample:
		csvwriter.writerow(row)
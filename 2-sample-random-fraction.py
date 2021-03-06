import csv
import random

records_list = []

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
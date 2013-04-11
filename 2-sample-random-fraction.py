import csv
import random

records_list = []

with open('ha-sequences.csv', 'rU') as f:
	records = csv.DictReader(f)
	
	for row in records:
		records_list.append(row)
	
	random.shuffle(records_list) #just coz I can lol
	
	"""Extract 1000 records randomly."""
	
	sample = random.sample(records_list, 1000)
	
	
with open('ha-sequences-sample.csv', 'w') as g:
	fieldnames = ['id', 'subtype', 'accession', 'strain_name', 'sequence']
	
	csvwriter = csv.DictWriter(g, delimiter = ',', fieldnames = fieldnames)
	csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
	for row in sample:
		csvwriter.writerow(row)
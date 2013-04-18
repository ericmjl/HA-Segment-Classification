"""The goal of this set of scripts is to identify how HA subtypes cluster with matrix protein subtypes."""

"""The goal of this script is to parse the sequences downloaded from fludb.org, and store them as a CSV file."""

from Bio import SeqIO
import csv

"""Open up the sequences and store them in memory as a dictionary. The structure of the dictionary is as follows:
    { 
        'id'         :record.id
        'sequence'   :record.seq
        'translation':record.seq.translate()"""
        
        
segment = 'HA'
filename_sequences = 'Influenza A Human Strains %s Protein Sequences.gb' % segment
filename_table_txt = 'Influenza A Human Strains %s Protein Sequences.txt' % segment
filename_table_csv = 'Influenza A Human Strains %s Protein Sequences.csv' %segment

# print filename
# because of legacy code, the elements all have "ha" before them where the code was not re-written. 
ha_sequences = open(filename_sequences, 'rU')
ha_db = []

for record in SeqIO.parse(ha_sequences, 'genbank'):
    ha_record = {}
    ha_record['id'] = record.id
    ha_record['sequence'] = record.seq
    ha_db.append(ha_record)
    
ha_sequences.close()

"""Convert the txt file into a csv file"""
import csv

in_file = open(filename_table_txt, 'rU')
out_file = open(filename_table_csv, 'w+')

in_txt = csv.reader(in_file, delimiter = "	")
out_csv = csv.writer(out_file)

for row in in_txt:
	out_csv.writerow(row)


"""Open up the HA data table (no sequences) that houses the strain name and subtype. Store strain name and accession number in the format that is identical to the sequence records for M (i.e. HM230702|A/Zhoushan/52/2009(H1N1))"""
file = open(filename_table_csv, 'rU')
ha_info = csv.DictReader(file)

ha_info_db = []

for row in ha_info:
	info = {}
	accession = row['Sequence Accession'].replace('*','')
	strain_name = row['Strain Name']
	subtype = row['Subtype']
	id = str(accession) + "|" + str(strain_name)
	
	info['id'] = id
	info['subtype'] = subtype
	info['accession'] = accession
	info['strain_name'] = strain_name
	
	ha_info_db.append(info)

"""Now, compare the information in ha_info_db to ha_db. If the id in the info_db is identical to the id in 'db', then add the subtype to 'ha_compiled'."""

ha_compiled = []

for strain in ha_db:
	for row in ha_info_db:
		if row['id'] == strain['id']:
			compiled = {}
			compiled['id'] = row['id']
			compiled['subtype'] = row['subtype']
			compiled['accession'] = row['accession']
			compiled['strain_name'] = row['strain_name']
			compiled['sequence'] = strain['sequence']
			
			ha_compiled.append(compiled)

"""Finally, write the data in the following formats:
	- CSV
	
First, write CSV file."""

fieldnames = ['id', 'subtype', 'accession', 'strain_name', 'sequence']
output_file = open('sequences.csv', 'w+')
csvwriter = csv.DictWriter(output_file, delimiter = ',', fieldnames = fieldnames)
csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
for row in ha_compiled:
	csvwriter.writerow(row)
output_file.close()

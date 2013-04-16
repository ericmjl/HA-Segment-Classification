"""The distance matrix contains an extraneous line first line, and needs to be converted into a CSV file format without manually doing so in Excel."""

import csv

in_file = open('sequences-distmat.txt', 'rU')



out_file = open('sequences-distmat.csv', 'w+')
in_txt = csv.reader(in_file, delimiter = " ")

out_csv = csv.writer(out_file)

#sanitize the data - remove any blanks cells in the table
sanitized_data = []
for num, row in enumerate(in_txt, 1):
# 	print num, row
	if num == 1:
		pass
	
	else:
		sanitized_row = []
		for element in row:
			if element != '':
				sanitized_row.append(element)
		sanitized_data.append(sanitized_row)


#Write the sanitized data out
for row in sanitized_data:
	out_csv.writerow(row)
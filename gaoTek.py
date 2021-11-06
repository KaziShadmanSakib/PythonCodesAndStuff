#Nov 6 10:03 PM

# Kazi Shadman Sakib
# Software Development Intern
# GaoTek Inc.

import csv
with open('ExportfromBitrix24Oct102021.csv', newline='') as csvfile:
	data = csv.DictReader(csvfile)
	f = open("Data.txt","w")
	i = 0
	for row in data:
		i = i + 1
		f.write(str(i))
		f.write(") ")

		f.write("First Name- ")
		f.write(row['First_Name'])
		f.write(", ")
		f.write("Last Name- ")
		f.write(row['Last_Name'])
		f.write(", ")
		
		f.write("Work EmailID- ")
		
		if row['Work_E-mail'] in (None, ""):
			f.write('Not Given')			
		else:
			f.write(row['Work_E-mail'])
		
		f.write(", ")
		
		f.write("Home EmailID- ")
		
		if row['Home_E-mail'] in (None, ""):
			f.write('Not Given')
		else:
			f.write(row['Home_E-mail'])
		f.write("\n")
	f.close()
#CSV
import csv

with open ('csv_fitxer.csv','w', encoding='utf-8') as csv_file:
   csv_writer = csv.writer(csv_file, delimiter='#')
   csv_writer.writerow(['Name', 'Surname', 'Age', 'Languages']) 
   csv_writer.writerow(['Guiller', 'Mas', '36', 'Python'])
   csv_writer.writerow(['Damià', 'Massip', '17', 'PSeint'])
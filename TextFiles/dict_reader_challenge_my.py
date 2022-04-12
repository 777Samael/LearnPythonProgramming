import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    sample = ""
    for line in range(3):
        sample += country_file.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    country_file.seek(0)

    reader = csv.DictReader(country_file, dialect=country_dialect)
    for row in reader:
        print(row)

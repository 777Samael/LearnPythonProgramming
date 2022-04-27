import csv

ordering = ['Country', 'Gold', 'Silver', 'Bronze', 'Rank']
# Note the lack of 'Total' in `ordering`

with open('OlympicMedals_2020.csv', encoding='utf-8', newline='') as data,\
        open('medals_dict.py', 'w', encoding='utf-8') as output_file:
    # Write the first part of the code (excluding the actual data)
    print('import csv', file=output_file)
    print(file=output_file)
    print('medals_table = [', file=output_file)

    reader = csv.DictReader(data)
    # Read each row from the CSV file, as a dictionary,
    # and produce a new dictionary containing the key/value
    # pairs we want, in the order we want.
    for row_dict in reader:
        new_dict = {}
        # Only print the values for the keys we want
        # (in the order we want them).
        for key in ordering:
            value = row_dict[key]
            if value.isnumeric():
                value = int(value)
            new_dict[key.casefold()] = value

        # print the dictionary to the output file
        # (indented by 4 spaces, with a trailing comma).
        print(f'    {new_dict},', file=output_file)

    # All the data rows have been written, print the terminating ]
    print(']', file=output_file)
    print(file=output_file)  # and finish with a blank line.

# Kylee Gordon Lab-21 04/27/2022

# This program reads data from a csv file and displays it formatted like a spreadsheet

import csv


def main():
    # csv file name
    filename = "lab21_excel.csv"

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    # printing the field names
    print('| '.join(field for field in fields))

    for row in rows[:csvreader.line_num]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" "),
        print('\n')


main()

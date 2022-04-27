# Kylee Gordon Lab-21 04/27/2022

# This program reads data from a csv file and displays it formatted like a spreadsheet

import csv


def main():
    # Setup
    filename = "lab21_excel.csv"
    headers = []
    rows = []

    # Input
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        headers = next(csvreader)

        for row in csvreader:
            rows.append(row)

    # Processing/Output
    # Print headers
    for col in headers:
        print("%-15s" % col, end=" "),
    print('\n')

    # Print rows
    for row in rows[:csvreader.line_num]:
        row_total = 0
        for col in row:
            print("%-15s" % col, end=" "),
        print('\n')


main()

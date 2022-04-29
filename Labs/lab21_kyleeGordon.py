# Kylee Gordon Lab-21 04/27/2022

# This program reads data from a csv file and displays it formatted like a spreadsheet
# It also calculates and displays the row and column totals

import csv


def main():
    # Setup
    filename = "lab21_excel.csv"
    rows = []

    # Input
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            rows.append(row)

    overall_total = 0

    # Processing/Output
    # Print rows
    for row in rows[:csvreader.line_num - 1]:
        for col in row:
            if col != "0.00":
                print("%-15s" % col, end=" "),
            else:
                total = calculate_row_total(row)
                print("%-15s" % total, end=" "),
                overall_total += total
        print('\n')

    # Print column totals
    print("%-15s" % "Total", end=" ")
    for x in range(1, 6):
        col_total = calculate_column_total(rows, x)
        print("%-15s" % col_total, end=" "),

    print("%-15s" % overall_total, end=" "),


def calculate_row_total(number_array):
    total = 0
    for x in range(1, len(number_array) - 1):
        total += float(number_array[x])
    return total


def calculate_column_total(rows, column_num):
    col_total = 0
    for x in range(1, len(rows)):
        col_total += float(rows[x][column_num])
    return col_total


main()

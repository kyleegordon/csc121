# Kylee Gordon Lab-18 04/18/2022

# This program reads the numbers in a file and calculates the average of those numbers.
# A missing file name will be handled with and IOError, and any non-numeric data
# in the file will be handled with a ValueError


def main():
    # Processing
    number_list = read_file()
    if len(number_list) > 0:
        total_sum = calculate_total(number_list)
        numbers_in_file = len(number_list)
        numbers_average = calculate_average(total_sum, numbers_in_file)
        # Output
        output(numbers_average)


def read_file():
    number_list = []
    try:
        file = open("exceptionNumbers.txt", "r")
        for x in file:
            try:
                current_num = int(x)
                number_list.append(current_num)
            except ValueError:
                print("This file contains data that is not numeric")
        file.close()
    except IOError:
        print("The file cannot be found")
    return number_list


def calculate_total(number_list):
    total = 0
    for x in number_list:
        total += x
    return total


def calculate_average(total, numbers_in_file):
    return total / numbers_in_file


def output(numbers_average):
    print("\nThe average of the numbers in this file is:  " + format(numbers_average, '.2f'))


main()

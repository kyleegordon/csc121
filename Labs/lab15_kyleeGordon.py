# Kylee Gordon Lab-15 04/05/2022

# This program asks the user how many random numbers should be created, then is creates a new file called
# randomNumbers.txt and writes each number to the file. Then it reads the numbers from the file and calculates
# the sum, quantity of numbers, average, highest number, and lowest number. Then it will print all the calculations.

import random


def main():
    # Input
    how_many_numbers = user_input()

    # Processing
    create_file()
    write_file(how_many_numbers)
    number_list = read_file()
    total_sum = calculate_total(number_list)
    numbers_in_file = calculate_numbers_in_file(number_list)
    numbers_average = calculate_average(total_sum, numbers_in_file)
    highest = get_highest(number_list)
    lowest = get_lowest(number_list)

    # Output
    output(total_sum, numbers_in_file, numbers_average, highest, lowest)


def user_input():
    how_many_numbers = 0
    while how_many_numbers < 13:
        how_many_numbers = int(input("How many random numbers would you like to add to the file? (minimum 13): "))
    return how_many_numbers


def create_file():
    file = open("randomNumbers.txt", "w")
    file.close()


def write_file(how_many_numbers):
    file = open("randomNumbers.txt", "w")
    for x in range(0, how_many_numbers):
        file.write(str(random.randint(1, 500)) + "\n")
    file.close()


def read_file():
    number_list = []
    file = open("randomNumbers.txt", "r")
    for x in file:
        number_list.append(int(x))
    file.close()
    return number_list


def calculate_total(number_list):
    total = 0
    for x in number_list:
        total += x
    return total


def calculate_numbers_in_file(number_list):
    return len(number_list)


def calculate_average(total, numbers_in_file):
    return total / numbers_in_file


def get_highest(number_list):
    highest = number_list[0]
    for x in number_list:
        if x > highest:
            highest = x
    return highest


def get_lowest(number_list):
    lowest = number_list[0]
    for x in number_list:
        if x < lowest:
            lowest = x
    return lowest


def output(total_sum, numbers_in_file, numbers_average, highest, lowest):
    print("\nThere are " + str(numbers_in_file) + " numbers in the file randomNumbers.txt\n")
    print("The total sum of these numbers is: " + str(total_sum) + "\n")
    print("The average is: " + format(numbers_average, '.2f') + "\n")
    print("The highest number is: " + str(highest) + "\n")
    print("The lowest number is: " + str(lowest) + "\n")


main()

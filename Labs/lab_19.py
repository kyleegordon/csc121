# Kylee Gordon Lab-19 04/25/2022

# This program reads a list of popular boy names and a list of girl names from separate files.
# The user can enter a name and the program will output whether the name was on one of the lists


def main():
    # Setup
    girl_names= read_file("GirlNames.txt")
    boy_names = read_file("BoyNames.txt")
    girl_total = 0
    boy_total = 0
    continue_program = True

    while continue_program:
        # Input
        current_name = input("Please enter a name: ")

        # Processing

        # Output



def read_file(file_name):
    file_content = []
    try:
        file = open(file_name, "r")
        for x in file:
            file_content.append(x)
        file.close()
    except IOError:
        print("The file cannot be found")
    return file_content



def output(numbers_average):
    print("\nThe average of the numbers in this file is:  " + format(numbers_average, '.2f'))


main()

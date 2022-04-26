# Kylee Gordon Lab-19 04/25/2022

# This program reads a list of popular boy names and a list of girl names from separate files.
# The user can enter a name and the program will output whether the name was on one of the lists


def main():
    # Setup
    girl_names = read_file("GirlNames.txt")
    boy_names = read_file("BoyNames.txt")
    girl_total = 0
    boy_total = 0
    total_names_checked = 0
    continue_program = 'y'

    while continue_program != 'x':
        # Input
        current_name = get_name()

        # Processing
        if current_name == '':
            continue
        total_names_checked += 1

        if check_list(current_name, girl_names):
            girl_total += 1
            print("\n" + current_name.capitalize() + " was on the list of popular girls names")
        else:
            print("\n" + current_name.capitalize() + " was not on the list of popular girls names")

        if check_list(current_name, boy_names):
            boy_total += 1
            print("\n" + current_name.capitalize() + " was on the list of popular boys names")
        else:
            print("\n" + current_name.capitalize() + " was not on the list of popular boys names")

        continue_program = input("\nEnter x to quit program, or any other key to continue: ")
        print("\n_______________________________________________________________")

    # Output
    output(total_names_checked, girl_total, boy_total)


def read_file(file_name):
    file_content = []
    try:
        file = open(file_name, "r")
        for x in file:
            x = x.lower().strip()
            file_content.append(x)
        file.close()
    except IOError:
        print("The file cannot be found")
    return file_content


def get_name():
    name = input("\nPlease enter a name: ")
    return name.lower()


def check_list(name, name_list):
    for x in name_list:
        if name == x:
            return True
    return False


def output(total_names_checked, girl_total, boy_total):
    print("\nA total of " + str(total_names_checked) + " names were checked")
    print("\n" + str(girl_total) + " of those names were on the list of popular girls names")
    print("\n" + str(boy_total) + " of those names were on the list of popular boys names")
    print("\nGoodbye")
    print("\n_______________________________________________________________")


main()

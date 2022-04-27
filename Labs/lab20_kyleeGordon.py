# Kylee Gordon Lab-20 04/26/2022

# This program ask the user to enter a positive integer, then displays all the numbers that are
# less than or equal to that number and states whether they are prime or composite


def main():
    while True:
        # Input
        number = get_number()

        # Processing/Output
        numbers_list = create_list(number)

        print("______________________________________________________________________________________")

        for x in numbers_list:
            is_prime(x)

        print("______________________________________________________________________________________")
        print("Follow the prompt below to continue this program or enter any negative number to exit")
        print("______________________________________________________________________________________")


# Collects user input
def get_number():
    need_input = True
    while need_input:
        try:
            number = int(input("Please enter an integer greater than 1: "))

            if number < 0:
                print("Cannot accept a negative integer. Goodbye.")
                exit()

            if number > 1:
                need_input = False
        except ValueError:
            print("Input must be an integer")

    return number


# Creates list starting at 2 and ending with highest_number
def create_list(highest_number):
    numbers_list = []
    for x in range(2, highest_number + 1):
        numbers_list.append(x)

    return numbers_list


# Determines and prints if number is prime or composite
def is_prime(number):
    for x in range(2, int(number / 2) + 1):
        if (number % x) == 0:
            print(str(number) + " is composite")
            return

    print(str(number) + " is prime")


main()

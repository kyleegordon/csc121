# Kylee Gordon Lab-17 04/07/2022

# This program accepts user input and determines if the input is numeric


def main():
    # Input
    user_input = input("Please enter anything to determine if it is numeric: ")

    # Processing
    if user_input == "":
        quit("This program has been terminated")
    is_numeric = is_number(user_input)

    # Output
    if is_numeric:
        print(user_input + " is a number")
    else:
        print(user_input + " is not a number")


def is_number(user_input):
    try:
        test_numeric = float(user_input)
        return True
    except:
        return False


main()

# Kylee Gordon Project 02 04/28/2022

# This program processes a tea shop's orders. It inputs from the customer the variety of tea,
# the size they would like, and their name. Then it outputs their order information
# including their name, price of the tea, sales tax, and the total amount owed

# Initialize Constant Variables
SALES_TAX = 0.045

# Tea Names
PLAIN_TEA = "Plain Tea"
BLACK_TEA = "Black Tea"
GREEN_TEA = "Green Tea"
WHITE_TEA = "White Tea"

# Tea Cost Per Ounce
PLAIN_CPO = 0.43
BLACK_CPO = 0.53
GREEN_CPO = 0.65
WHITE_CPO = 0.78


def main():
    # NEED TO MODIFY MULTIPLE ORDER FUNCTIONALITY TO RANDOMLY GENERATE ORDER DETAILS
    continue_order = True

    while continue_order:
        action_choice = display_start_menu()

        if action_choice == 1:
            continue_order = False
            num_orders = 1
        elif action_choice == 2:
            num_orders = 0
            while num_orders > 10 or num_orders < 1:
                try:
                    num_orders = int(input("Enter number of orders (Min: 1 - Max: 10)"))
                except ValueError:
                    print("Input must be a numeric integer")
        elif action_choice == 3:
            print("Thank you for using our program. Goodbye.")
            exit()

        for x in range(0, num_orders):
            chosen_tea = select_tea()
            cost_per_oz = determine_cost_per_oz(chosen_tea)
            cup_size = determine_tea_size()
            cust_name = input("Enter a name for the order: ")
            subtotal = calculate_price_tea(cost_per_oz, cup_size)
            tax = calculate_sales_tax(subtotal)
            total_cost = calculate_total_bill(subtotal, tax)
            display_bill(subtotal, tax, total_cost, cust_name)


def display_start_menu():
    print("Welcome to the World's Best Tea Shop")
    print("1 - Process a Single Order")
    print("2 - Process Multiple Orders")
    print("3 - Quit")

    # ADD ERROR HANDLING TO ENSURE PROPER SELECTION IS MADE

    return int(input("Enter choice of action: "))


def select_tea():
    global PLAIN_TEA, WHITE_TEA, GREEN_TEA, WHITE_TEA
    print("1 - " + str(PLAIN_TEA))
    print("2 - " + str(BLACK_TEA))
    print("3 - " + str(GREEN_TEA))
    print("4 - " + str(WHITE_TEA))

    selection = int(input("Enter choice of tea: "))

    if selection == 1:
        return PLAIN_TEA
    elif selection == 2:
        return BLACK_TEA
    elif selection == 3:
        return GREEN_TEA
    elif selection == 4:
        return WHITE_TEA
    else:
        print("ERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        quit()


def determine_cost_per_oz(tea_variety):
    if tea_variety == PLAIN_TEA:
        return PLAIN_CPO
    elif tea_variety == BLACK_TEA:
        return BLACK_CPO
    elif tea_variety == GREEN_TEA:
        return GREEN_CPO
    elif tea_variety == WHITE_TEA:
        return WHITE_CPO
    else:
        print("ERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        quit()


def determine_tea_size():
    print("\n1 - Small (8oz)")
    print("2 - Medium (16 oz)")
    print("3 - Large (24 oz)")

    selection = int(input("Enter choice of size: "))

    if selection == 1:
        return 8
    elif selection == 2:
        return 16
    elif selection == 3:
        return 24
    else:
        print("ERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        quit()


def calculate_price_tea(cost_per_oz, cup_size):
    return cost_per_oz * cup_size


def calculate_sales_tax(subtotal):
    global SALES_TAX
    return subtotal * SALES_TAX


def calculate_total_bill(subtotal, tax):
    return subtotal + tax


def display_bill(subtotal, tax, total_cost, cust_name):
    print("\n" + cust_name)
    print("Price of Tea: $" + format(subtotal, '.2f'))
    print("Sales Tax: $" + format(tax, '.2f'))
    print("Total Amount Owed: $" + format(total_cost, '.2f') + "\n")


main()

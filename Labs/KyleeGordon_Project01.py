# Kylee Gordon Project 01 02/18/2022

# This program handles a tea shop's orders. It inputs from the customer the variety of tea,
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

# Input
print("Welcome to the World's Best Tea Shop")
print("1 - " + str(PLAIN_TEA))
print("2 - " + str(BLACK_TEA))
print("3 - " + str(GREEN_TEA))
print("4 - " + str(WHITE_TEA))

selection = int(input("Enter choice of tea: "))

if selection == 1:
    chosenTea = PLAIN_TEA
    costPerOunce = PLAIN_CPO
elif selection == 2:
    chosenTea = BLACK_TEA
    costPerOunce = BLACK_CPO
elif selection == 3:
    chosenTea = GREEN_TEA
    costPerOunce = GREEN_CPO
elif selection == 4:
    chosenTea = WHITE_TEA
    costPerOunce = WHITE_CPO
else:
    print("ERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
    quit()

print("\n1 - Small (8oz)")
print("2 - Medium (16 oz)")
print("3 - Large (24 oz)")

selection = int(input("Enter choice of size: "))

if selection == 1:
    cupSize = 8
elif selection == 2:
    cupSize = 16
elif selection == 3:
    cupSize = 24
else:
    print("ERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
    quit()

customerName = input("\nEnter the name of the customer: ")

# Processing
subtotal = cupSize * costPerOunce
tax = subtotal * SALES_TAX
totalCost = subtotal + tax

# Output

print("\n" + customerName)
print("Price of Tea: $" + format(subtotal, '.2f'))
print("Sales Tax: $" + format(tax, '.2f'))
print("Total Amount Owed: $" + format(totalCost, '.2f'))

# Kylee Gordon Lab-12 03/18/2022

# This program calculates the total gallons of paint, labor hours, cost of paint,
# cost of labor, and total cost of the paint job. It uses the number of rooms to
# be painted and the square footage of each room to make these calculations.
# This program assumes that every 225 square feet of wall required 1 gallon of
# paint and 4 hours of labor. The cost of labor is $35/hour. It will input the
# cost per gallon of paint from the user at a minimum of $10/gallon.

import math

# Global Variables
gallons_paint = 0
labor_hours = 0
total_paint_cost = 0
total_labor_cost = 0


def main():
    # Input
    total_sqft = num_rooms()
    price_per_gallon = paint_price()

    # Processing
    total_cost = calc_cost(total_sqft, price_per_gallon)

    # Output
    print_results(total_cost)


# This function collects user input to determine the number of rooms
# and the square footage of each room that needs to be painted
def num_rooms():
    total_rooms = 0
    while total_rooms < 1:
        total_rooms = int(input("How many rooms do you need to paint?"))

    sum_sqft = 0
    for x in range(1, total_rooms + 1):
        sqft = 0

        while sqft < 1:
            sqft = int(input("How many square feet are in room " + str(x) + "?"))

        sum_sqft += sqft

    return sum_sqft


# This function collects user input to determine the cost per gallon of paint
def paint_price():
    price_per_gallon = float(input("What is the price of each gallon of paint? (Minimum $10) : $"))
    if price_per_gallon >= 10:
        return price_per_gallon
    else:
        paint_price()


# This function calculates the gallons of paint required, hours of labor required, cost of paint,
# cost of labor, and returns the total cost of the job
def calc_cost(total_sqft, price_per_gallon):
    global gallons_paint, labor_hours, total_paint_cost, total_labor_cost
    gallons_paint = int(math.ceil(total_sqft / 225))
    labor_hours = total_sqft / 225 * 4
    total_paint_cost = gallons_paint * price_per_gallon
    total_labor_cost = labor_hours * 35
    return total_labor_cost + total_paint_cost

# This function prints the gallons of paint required, labor hours required, cost of paint, cost of labor, and total cost
def print_results(total_cost):
    print("This paint job requires: " + str(gallons_paint) + " gallons of paint and " + format(labor_hours, '.2f') + " hours of labor\n")
    print("The costs for this job will be:\n")
    print("Cost of Paint: $" + format(total_paint_cost, '.2f'))
    print("\nCost of Labor: $" + format(total_labor_cost, '.2f'))
    print("\nTotal Cost: $" + format(total_cost, '.2f'))


main()

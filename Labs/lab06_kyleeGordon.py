# Kylee Gordon Lab-06 02/06/2022

# This program asks the user how many software packages that they would like to buy
# and calculates the appropriate discount. Each software package has a bas price of $77.
# An 8.5% discount is applied to purchases of 9-23 packages, 22.5% discount applied to
# purchases of 24-41 packages, 32.5% discount to purchases of 42-88 packages,
# and a 39.5% discount to purchases of 89 or more packages.


# Input
totalSold = int(input("How many software packages would you like to purchase?"))
totalCost = 77 * totalSold
discountedCost = totalCost
discountPercent = 0

# Processing
if 9 <= totalSold <= 23:
    discountPercent = 8.5
elif 24 <= totalSold <= 41:
    discountPercent = 22.5
elif 42 <= totalSold <= 88:
    discountPercent = 32.5
elif totalSold >= 89:
    discountPercent = 39.5

discountedCost = totalCost * (1 - (discountPercent/100))
discount = totalCost - discountedCost

# Output
print("Quantity Purchased: " + str(totalSold))
print("Cost Before Discount: $" + format(totalCost, '.2f'))
print("Discount Amount: $" + format(discount, '.2f'))
print("Cost After Discount: $" + format(discountedCost, '.2f'))

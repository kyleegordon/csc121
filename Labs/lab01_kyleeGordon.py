# Kylee Gordon Lab-01 01/18/2022

# This program asks the user how many cookies they would like to bake,
# then it performs calculations on the original recipe and outputs
# the amount of each ingredient required to bake the number of
# cookies that the users has requested

# Assign ingredient amounts from the original  recipe
sugar = 2.5
butter = 1.75
flour = 3.75

# Input
numCookies = float(input('How many cookies would you like to bake?'))

# Processing
conversion = numCookies / 63
newSugar = sugar * conversion
newButter = butter * conversion
newFlour = flour * conversion

# Output
print("To make " + str(numCookies) + " cookies, you will need:")
print(str(newSugar) + " cups of sugar")
print(str(newButter) + " cups of butter")
print(str(newFlour) + " cups of flour")
# Kylee Gordon Lab-04 01/29/2022

# This program calculates the minimum number of packages of hot dogs and buns required
# to serve a given number of people and hot dogs allowed per person.
# It assumes that there are 10 hot dogs per package and 8 buns per package.

import math

# Input
numPeople = int(input("How many people will you be serving?"))
hotDogsPerPerson = int(input("How many hot dogs will be served to each person?"))

# Processing
minHotDogs = numPeople * hotDogsPerPerson
hotDogsPerPackage = 10
bunsPerPackage = 8
minHotDogPackages = int(math.ceil(minHotDogs / hotDogsPerPackage))
minBunPackages = int(math.ceil(minHotDogs / bunsPerPackage))
leftOverHotDogs = (hotDogsPerPackage * minHotDogPackages) - minHotDogs
leftOverBuns = (bunsPerPackage * minBunPackages) - minHotDogs

# Output
print("\nTo feed " + str(numPeople) + " people " + str(hotDogsPerPerson) + " hot dogs each: ")
print("You will need " + str(minHotDogPackages) + " packages of hot dogs and "
      + str(minBunPackages) + " packages of buns")
print("There will be " + str(leftOverHotDogs) + " hot dogs and " + str(leftOverBuns) + " buns leftover")

# Kylee Gordon Lab-08 02/14/2022

# This program produces a bar chart that represents population growth of Dustyville.
# It accepts keyboard input for the population of the 5 census years between 1900-2000.
# One asterisk will be displayed for each 1000 people in the population at each
# census year.


# Input/Processing
year = [1900, 1920, 1940, 1960, 1980, 2000]
asteriskByYear = {}

for x in range(0, 6):
    population = int(input("What was the population in the year " + str(year[x]) + "?"))
    numAsterisks = int(population / 1000)

    asteriskDisplay = ''
    for i in range(0, numAsterisks):
        asteriskDisplay += '*'

    asteriskByYear[x] = asteriskDisplay

# Output
print("\nDustyville Population Growth\n(each * represents 1,000 people)")

for j in range(0, 6):
    print(str(year[j]) + ' ' + str(asteriskByYear[j]))

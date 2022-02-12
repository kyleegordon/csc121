# Kylee Gordon Lab-02 01/23/2022

# This program calculates compound interest gained in a savings account
# based on the formula A = P(1+ (r/n))^(n*t)
# It inputs the amount of money originally deposited (P), the annual interest rate (r),
# the number of times per year the interest is compounded (n), and the number of
# years (t) till the money will be withdrawn. It uses that info to calculate the
# amount of interest gained and outputs the original deposit amount, the annual interest
# rate, and the total amount of money at the end of the specified time period

# Input
print("Let's calculate the amount of money your savings account will gain")
principle = float(input("How much money did you originally deposit?"))
rate = float(input("What is the annual interest rate percentage?"))
rate /= 100 # converts rate to a decimal
timesPerYear = float(input("How many times per year is the interest compounded? (monthly = 12, quarterly = 4, etc.)"))
years = float(input("How many years will your money be in this account?"))

# Processing
totalAmount = principle * ((1 + (rate / timesPerYear))**(timesPerYear * years))

# Output
print("\nWith an original deposit of $" + format(principle, '.2f'))
print("And an annual interest rate of " + str(rate * 100) + "%")
print("You will have $" + format(totalAmount, '.2f') + " after " + str(years) + " years.")

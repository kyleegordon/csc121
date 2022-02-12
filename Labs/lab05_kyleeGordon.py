# Kylee Gordon Lab-05 01/29/2022

# This program asks the user to input a number of seconds and
# converts it into days, hours, minutes, and seconds as needed


# Input
seconds = int(input("Please enter a number of seconds: "))

# Processing
print("\n" + str(seconds) + " seconds is equal to : ")
result = ""

if seconds >= 86400:
    result += "\nDays: " + str(seconds // 86400)
    seconds %= 86400

if seconds >= 3600:
    result += "\nHours: " + str(seconds // 3600)
    seconds %= 3600

if seconds >= 60:
    result += "\nMinutes: " + str(seconds // 60)
    seconds %= 60

if seconds > 0:
    result += "\nSeconds: " + str(seconds)

# Output
print(result)

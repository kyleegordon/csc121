# Kylee Gordon Lab-09 02/15/2022

# This program uses loops to diplay Pattern A, a right side up triangle, and
# Pattern B, an upside down triangle


# Processing/Output
print("Pattern A")
for x in range(1, 11):
    for y in range(0, x):
        print('+', end='')
    print('')

print('\nPattern B')
for i in reversed(range(1, 11)):
    for j in range(0, i):
        print('+', end='')
    print('')





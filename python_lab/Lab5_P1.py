# A year is a leap year if it is divisible by 4, but years divisible by 100
# are not leap years unless they are also divisible by 400. 
# Write a program that asks the user to input a year and then determines whether that year is a leap year or not.

# Input
# The input consists of a single line containing one integer, ranging from 0 to 105
i = int(input())
is_leap_year = False
if i % 4 == 0:
    is_leap_year = True
    # Years divisible by 100 are not leap years unless they are also divisible by 400. 
    if i % 100 == 0:
        if i % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
        
# Output
# Print a boolean value to conclude whether the given year is a leap year or not.
print(is_leap_year)


# C. Problem 3: Sum of Digits in Even Positions
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer, and your task is to calculate the sum of the digits that appear in even positions (index starting from 0, from right to left) within that integer. If the integer is negative, convert it to a positive number before calculating the sum. The solution must be implemented using recursion.

# Function template:
def get_digit(n: int, position) -> int:
    return int(str(n)[-1-position])

def sum_of_digits(num : int, position=0) -> int:
    # Your implementation is here
    
    # print("cALLED TO SUM", num, position)
    if position >= len(str(num)):
        return 0 
    return get_digit(num, position) + sum_of_digits(num, position+2)

# Input
# The input consists of a single integer n
#  where −109≤n≤109
# .
n = int(input())
n = abs(n)
# Output
# Output the sum of digits that are at even positions (starting from 0) when the number is read from right to left.


print(sum_of_digits(n))
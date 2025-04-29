# Write a Python function that sorts three given numbers in ascending order (smallest to largest).

# Input
# The input consists of a single line containing three integers, ranging from −109 to 109
# , separating by a space character.
i = input()
i = i.split(" ")
a, b, c = map(int, i)

def swap(first, second):
    return second, first

# These combonations of checks always sort the 3 numbers correctly
if a > b:
    a, b = swap(a, b)
if b > c:
    b, c = swap(b, c)
if a > b:
    a, b = swap(a, b)

# Output
# Three numbers in ascending order.
print(a, b, c)

# Examples
# Input
# 3 1 2
# Output
# 1 2 3
# Input
# 10 20 -5
# Output
# -5 10 20
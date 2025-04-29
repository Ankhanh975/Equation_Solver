# Lab 07: Lists, iteration, and loops
# Problem 1: Star Pyramid

# A Python program that takes an integer n as input and draws the n-row hollow pyramid.
# Input Format:
# Player list: A single integer n which satisfies 3 ≤ n ≤ 100.

i = int(input())

def star_pyramid(n: int) -> str:
    # Description:
    # An n-row star pyramid is a solid triangle which has n rows and contains asterisks (*). For example, 5-row hollow pyramid can be display as:
    # *
    # ***
    # *****
    # *******
    # *********
    output_string = ""
    # Fix python indexing
    n = n + 1
    for x in range(n):
        num_of_white_space = n - x - 1
        white_spaces = " " * num_of_white_space


        output_string += white_spaces + "*" * (2 * x - 1) + "\n"
    return output_string

# Expected Output:
# A solid star pyramid composed of n rows, with each row containing an increasing number of asterisks.

print(star_pyramid(i))
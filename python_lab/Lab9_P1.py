# Problem 1: Counting Sort
# Description:
# Given an unsorted list of integers, implement the Counting Sort algorithm to sort the list in ascending
# order. Your task is to complete the following sub-problems:
# Part (a): Find the Minimum and Maximum Values
# Write a function named find min max that takes the integer list as the input and returns the minimum
# and maximum values in the list. For example, given the input [4, 3, 2, 5, 3, 4, 1, -1], the function
# will return -1 5.
def find_min_max(Z: list) -> list[int]:
    m1 = float("inf")
    m2 = float("-inf")
    for x in Z:
        m1 = min(m1, x)
        m2 = max(m2, x)
    return [m1, m2]

# print(find_min_max([4, 3, 2, 5, 3, 4, 1, -1])) 
# Part (b): How many times does an element appear in the list?
# Write a function named merge two list that counts the number of times each element appears in the
# list. Specifically, this function:
# • Receives the original list and its minimum and maximum values.
# • Creates a counting list that starts at the minimum value and ends at the maximum value.
# • Populates the counting list with the occurrences of each element adjusted for the range offset by
# the minimum value.
# For example, given the original list [4, 3, 2, 5, 3, 4, 1, -1] with -1 and 5 are minimum and maximum numbers, the function will return [1, 1, 1, 2, 2, 1].
def count_frequency(Z: list, m1: int, m2: int):
    r = [0] * (m2 - m1 + 1)
    for x in Z:
        r[x - m1] += 1
    return r

# print(count_frequency([4, 3, 2, 5, 3, 4, 1, -1], -1, 5))

# Part (c): Counting Sort
# Task: Write a function named counting sort that takes an unordered list as the input and returns the
# sorted list in ascending order. The function needs to apply the above-built functions in Parts (a) and
# (b). For example, given the unordered lists [4, 3, 2, 5, 3, 4, 1, -1], the function will return [-1,
# 1, 2, 3, 3, 4, 4, 5].
def counting_sort(Z: list):
    m1, m2 = find_min_max(Z)
    r = []
    frequency = count_frequency(Z, m1, m2)
    for i, x in enumerate(frequency):
        for y in range(x):
            r.append(i + m1)
    return r

# print(counting_sort([4, 3, 2, 5, 3, 4, 1, -1]))
# Input:
# A list of integers, separated by space, each number ranges from −100 to 100. The amount of integers
# ranges from 2 to 100.
i = input()
# i = "4 3 2 5 3 4 1 -1"
i = i.split()
i = map(int, i) 
i = list(i)
print(i)

# Output:
# The outputs should consist of the following lines:
# • The first line describes the minimum and maximum values of the given list.
print(*find_min_max(i))
# • The second line shows the counting list from Part (b).
print(count_frequency(i, *find_min_max(i)))
# • The third line returns the fully sorted list.
print(counting_sort(i))

# import time
# i = "4 3 2 5 3 4 1 -1"
# i = i.split()
# i = map(int, i) 
# i = list(i)
# n = i
# start_time = time . perf_counter ()
# mean = counting_sort(n)
# end_time = time . perf_counter ()
# print(end_time - start_time)



# Comments these results at the end of the program

"""
 Input : 4 3 2 5 3 4 1 -1
 Execution Time : 6.479991134256124e-05 seconds

 Input : 4 3 2 5 3 4 1 -1 4 3 2 5 3 4 1 -1 4 3 2 5 3 4 1 -1 4 3 2 5 3 4 1 -1
 Execution Time : 16.18-05 seconds
"""
# D. Problem 4: Number of Distinct Elements in a Subarray
# Given an array of integers. Find the maximum number of distinct elements in any subarray of size k
# . A subarray is a contiguous sequence of elements in the array.

# Input
N = input()
second_line = input()
K = input()


# N = "7"
# second_line = "4 1 2 1 1 2 3"
# K = "3"

# The first line contains an integer n (1≤n≤105), the size of the array.
N = int(N)
# The second line contains n integers, representing the elements of the array.
second_line = second_line.split(" ")
second_line = map(lambda x: int(x), second_line)
second_line = list(second_line)
# The third line contains an integer k, (1≤k≤n), the size of the subarray.
K = int(K)

sub_arrays = []
max_length = 0
for x in range(0, N - K + 1):
    sub_array = second_line[x: x + K]
    sub_array = set(sub_array)
    sub_array = len(sub_array)
    max_length = max(sub_array, max_length)

print(max_length)
# Output: Print the maximum number of distinct elements in any subarray of size k

# Examples
# Input

# 7
# 4 1 2 1 1 2 3
# 3
# Output
# 3

# Input
# 5
# 1 2 1 3 4
# 5
# Output
# 4
# Note
# Explanation: In the first test case, the subarray [1, 2, 3] has 3 distinct elements. In the second test case, the entire array has 4 distinct elements.



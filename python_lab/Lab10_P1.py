# Problem 1: Finding the nth Fibonacci Number
# Description:
# Write two functions to calculate the nth Fibonacci number.
# • The first function fibonacci sequential(n) calculates the nth Fibonacci number using a sequential
# (iterative) approach.
# • The second function fibonacci recursive(n) calculates the nth Fibonacci number using a recursive
# approach.
# The Fibonacci sequence is defined as follows:
# F(0) = 0, F(1) = 1, and F(n) = F(n − 1) + F(n − 2) for n > 1

# Function to calculate nth Fibonacci number using an iterative approach
def fibonacci_sequential(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev, curr = 0, 1
    for i in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr

# Function to calculate nth Fibonacci number using a recursive approach
def fibonacci_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Input reading
n = int(input())

# Output the results from both functions
print("Sequential:", fibonacci_sequential(n))
print("Recursive:", fibonacci_recursive(n))

# Input:
# The input consists of a single line containing a non-negative integer n (0 ≤ n ≤ 40).
# Output:
# The output should be the nth Fibonacci number calculated by both functions, each on a separate line. Please
# see the example for the output format.
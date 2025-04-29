# B. Problem 2: Printing a Pattern

# Write two functions to print a pattern of stars (*) as shown in the example. The pattern has n rows.

# The first function print_pattern_sequential(n) prints the pattern using a sequential (iterative) approach.
def print_pattern_sequential(n: int) -> str:
    s = ""
    for x in range(n+1):
        s += "*"*x + "\n"
        
    s = s[1:-1]
    return s

def print_pattern_recursive(n: int, row = 1):
    def _print_pattern_recursive(n: int, row = 1) -> str:
        if row == n+1:
            return "*"
        else:
            # print("debug", "*"*(n - row) + "\n" + _print_pattern_recursive(n, row = row + 1))
            return "*"*(row) + "\n" + _print_pattern_recursive(n, row = row + 1)
    s = _print_pattern_recursive(n, row)
    return s[:-2]

# print(print_pattern_recursive(10))
# print(len(print_pattern_recursive(10).split("\n")))

# The second function print_pattern_recursive(n, row=1) prints the pattern using a recursive approach.
# Input
# The input consists of a single line containing a positive integer n
#  (1≤n≤100
# ).
i = int(input())
# i=10

# Output
# The output should be printed in two separate lines, one for each function. Please see the example for the output format.
print("Sequential:")
print(print_pattern_sequential(i))
print("Recursive:")
print(print_pattern_recursive(i))


# # Your code for the problem
# ...
# ...
# ...


# # Comment the execution time results
# """
# Input: 10
# Sequential: 3628800
# Execution Time (Sequential): 0.00009125 seconds
# Recursive: 3628800
# Execution Time (Recursive): 0.00001333 seconds

# Input: 20
# Sequential: 2432902008176640000
# Execution Time (Sequential): 0.00005829 seconds
# Recursive: 2432902008176640000
# Execution Time (Recursive): 0.00001754 seconds
# """


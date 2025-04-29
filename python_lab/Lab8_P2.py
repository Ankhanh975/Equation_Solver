# B. Problem 2: Employee Work Hours
# You are given a list of employees, and each employee's data containing their name and the number of hours they worked for each day of the week (7 integers). Your task is to perform the following steps:

# Read the data for each employee and store it in a tuple (name, [hours1, hours2, ..., hours7]).
# Input
# The first line contains an integer n
#  (1≤n≤100)
#  representing the number of employees. The following n lines contain the employee data in the format: name, hours1, hours2, hours3, hours4, hours5, hours6, hours7, , where name
#  is a string and hours1,hours2,…,hours7
#  are integers representing the hours worked each day.

# N = input()
# N = int(N)
# i = []
# for x in range(N):
#     i.append(input())

N = 3
i = ["John 8 8 8 8 8 0 0",
"Jane 9 9 9 9 9 4 4",
"Doe 6 6 6 6 6 6 6"]
i = map(lambda x: x.split(" ", 1), i)
i = list(i)
i = map(lambda x: [x[0], x[1].split(" ")], i)
i = list(i)
i = map(lambda x: tuple([x[0], list(map(lambda x: int(x), x[1]))]), i)
i = list(i)
i = map(lambda x: tuple([x[0], sum(x[1])]), i)
# Calculate the total hours worked for each employee over the week.
i = list(i)
i = filter(lambda x: x[1] > 40, i)
# Identify employees who have worked more than 40 hours.
i = list(i)
i = sorted(i, key = lambda x: [-x[1], x[0]])
# Sort the employees based on their total hours worked in descending order, and if two employees have the same total hours, sort them based on their names in ascending order.
i = list(i)

# Output the sorted list of employees with their names and total hours worked, separated by a comma (only for employees who worked more than 40 hours).
print(i)
# Output
# Output the sorted list of employees based on their total hours worked. Each employee should be represented as a tuple (name,total_hours)
# , with elements separated by a comma and a space. If there are no employees who worked more than 40 hours, output an empty list.

# Examples
# Input
# 3
# John 8 8 8 8 8 0 0
# Jane 9 9 9 9 9 4 4
# Doe 6 6 6 6 6 6 6
# Output
# [('Jane', 53), ('Doe', 42)]
# Input
# 3
# John 12 12 12 5 0 0 0
# Doe 0 0 0 5 12 12 12
# Charles 0 0 0 4 12 12 12
# Output
# [('Doe', 41), ('John', 41)]
# Input
# 2
# John 12 12 12 4 0 0 0
# Doe 0 0 0 4 12 12 12
# Output
# []


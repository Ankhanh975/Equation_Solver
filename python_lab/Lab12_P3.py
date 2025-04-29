# C. Employee Management System
# Task is to create a system to manage employees with the following instructions: 
# Create base class Employee and two subclasses: FullTimeEmployee and PartTimeEmployee. 
# Each subclass will implement a method to calculate the salary based on different salary calculation 
# formulas.

# 'Employee' (Base Class): The Employee class represents a general employee and 
# should include the following methods:
# A private attribute __name that stores the name of the employee.
# A private attribute __employee_id that stores the unique identifier for the employee.
# A method calculate_salary() that raises a NotImplementedError. This will be overridden 
# by the subclasses.
class Employee:
    def __init__(self, employee_id, name):
        self._name = name
        self._employee_id = employee_id
    
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary method")
    
# 'FullTimeEmployee' (Class): The FullTimeEmployee class inherits from the Employee class and 
# represents a full-time employee. This class should include:
# An additional attribute monthly_salary, which stores the monthly salary for full-time employees.
# An overridden calculate_salary() method that returns the monthly_salary.
class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self._monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self._monthly_salary
    
# 'PartTimeEmployee' (Class): The PartTimeEmployee class inherits from the Employee class 
# and represents a part-time employee. This class should include:
# An additional attribute hourly_rate, which stores the hourly rate for part-time employees.
# An additional attribute hours_worked, which stores the total hours worked in a given period.
# An overridden calculate_salary() method that calculates the salary as hourly_rate ×
#  hours_worked.
class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked
    
    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

if __name__ == "__main__":
    # Input
    # The input consists of multiple lines:
    # The first line contains an integer (n) ((1 <= n <= 10)), representing the number 
    # of employee records.
    # The following (n) lines contain employee information in the format:
    # For a FullTimeEmployee, input the employee ID, name, and monthly salary.
    # For a PartTimeEmployee, input the employee ID, name, hourly rate, and hours worked.
    n = int(input().strip())
    employees = []

    for _ in range(n):
        inputs = input().strip().split()
        
        if len(inputs) == 3:  # Full-time employee
            employee_id, name, monthly_salary = inputs
            employee = FullTimeEmployee(int(employee_id), name, float(monthly_salary))
        else:  # Part-time employee
            employee_id, name, hourly_rate, hours_worked = inputs
            employee = PartTimeEmployee(int(employee_id), name, float(hourly_rate), float(hours_worked))
        
        employees.append(employee)

    # Output
    # For each employee, print the employee ID, name, and calculated salary.
    for employee in employees:
        salary = employee.calculate_salary()
        print(f"Employee ID: {employee._employee_id}, Name: {employee._name}, Salary: {salary}")

# Example
# Input: 
# 3
# John 5000
# Alice 20 120
# Bob 3000
# Output:
# Employee ID: 1, Name: John, Salary: 5000.0
# Employee ID: 2, Name: Alice, Salary: 2400.0
# Employee ID: 3, Name: Bob, Salary: 3000.0
import math

def solve_quadratic (a: float, b: float , c:float) -> str:
    # Input: a, b, c representing the coefs of a quadratic equation
    # Output: string representing the solutions of the quadratic equation
    
    print("Attempted to solve the equation.")
    
    try:
        discriminant = b **2 - 4* a * c
        if discriminant < 0:
            return "Error: No real solutions"
        else :
            root1 = (- b + math.sqrt(discriminant)) / (2 * a)
            root2 = (- b - math.sqrt(discriminant)) / (2 * a)
        return f"Solutions: {root1}, {root2}"
    except ZeroDivisionError:
        # This error occurs when a = 0, in this case the quadratic formula can not be applied but
        # the linear formula should be used instead 
        root1 = - c / b
        return f"Linear equation, solutions: {root1}"


if __name__ == "__main__":
    # Take the input to be solve using the quadratic formula
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve_quadratic(a, b, c))
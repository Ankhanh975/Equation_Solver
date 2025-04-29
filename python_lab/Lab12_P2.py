# B. Polynomial Representation
# Class Polynomial to represent polynomials. Implement addition and multiplication using operator overloading.

# Polynomial (Base Class):
# Attributes:
# coefficients (list of integer): Stores the coefficients of the polynomial (include constant coefficients) in ascending order of powers. For example, the input [1, 2, 3] represents (1 + 2x + 3x^2).
# Methods:
# __init__(self, coefficients): Constructor to initialize the list of coefficients.
# __add__(self, other): Overloads the + operator to add two polynomials. Aligns the coefficients of both polynomials and returns a new Polynomial object.
# __mul__(self, other): Overloads the * operator to multiply two polynomials. Performs polynomial multiplication and returns a new Polynomial object.
# degree(self): A helper method to return the degree of the polynomial (the highest power with a non-zero coefficient). This function is used in __add__ and __mul__ function
# __str__(self): Overrides the __str__ method to return the polynomial in standard mathematical notation.
class Polynomial:
    def __init__(self, coefficients):
        # Remove leading zeros
        while coefficients and coefficients[-1] == 0:
            coefficients.pop()
        self.coefficients = coefficients or [0]
    
    def __add__(self, other):
        # Pad shorter list with zeros
        max_length = max(len(self.coefficients), len(other.coefficients))
        a = self.coefficients + [0] * (max_length - len(self.coefficients))
        b = other.coefficients + [0] * (max_length - len(other.coefficients))
        
        result = [a[i] + b[i] for i in range(max_length)]
        return Polynomial(result)
    
    def __mul__(self, other):
        result_length = len(self.coefficients) + len(other.coefficients) - 1
        result = [0] * result_length
        
        # Multiply each term
        for i, coef1 in enumerate(self.coefficients):
            for j, coef2 in enumerate(other.coefficients):
                result[i+j] += coef1 * coef2
        
        return Polynomial(result)
    
    def degree(self):
        return len(self.coefficients) - 1
    
    def __str__(self):
        if not self.coefficients or all(c == 0 for c in self.coefficients):
            return "0"
        
        terms = []
        for power, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            
            if power == 0:
                terms.append(f"{coef}" if coef > 0 else f"{str(coef)[:1]} {str(coef)[1:]}")
            elif power == 1:
                terms.append(f"{coef}x" if coef != 1 else "x")
            else:
                terms.append(f"{coef}x^{power}" if coef != 1 else f"x^{power}")
                
            terms.append(f" + ")
        
        return_string = "".join(terms)
        return_string = return_string.replace("+ -", "- ")  
        return_string = return_string.replace(" 1x^", " x^")
        return return_string[:-3]

if __name__ == "__main__":
    # Input
    # Two polynomials are provided as lists of coefficients (e.g., 1 2 3 for (1 + 2x + 3x^2)). The number of elements in each list is less than 10
    coeffs1 = list(map(int, input().strip().split()))
    coeffs2 = list(map(int, input().strip().split()))
    # coeffs1 = list(map(int, "3 -1 4 2".split()))
    # coeffs2 = list(map(int, "-2 3".split()))

    poly1 = Polynomial(coeffs1)
    poly2 = Polynomial(coeffs2)
    
    sum_poly = poly1 + poly2
    product_poly = poly1 * poly2
    
    # Output
    # The sum of the two polynomials.
    # The product of the two polynomials.
    print(f"Sum: {sum_poly}")
    print(f"Product: {product_poly}")

    

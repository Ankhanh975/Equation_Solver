# D. Fraction is simple
# A fraction number A/B has two components, A is the numerator part and B is the denominator part. 
# Create a Fraction class and enable arithmetic operations, including add, and multiply by 
# the following parts:

class Fraction:
    def __init__(self, numerator, denominator):
        # Part (a): Initialization} Initiate the class with an __init__ function that accepts:
        # A class attribute __numerator, which is the numerator part of the fraction, obtaining the value of the input argument numerator, a positive integer.
        # A class attribute __denominator, which is the denominator part of the fraction, obtaining the value of the input argument denominator, a positive integer.

        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        # Part (b): Fraction Methods
        # Define method display that prints the fraction in the form of __numerator/__denominator.
        print(f"{self.numerator}/{self.denominator}")

    def add(self, other):
        # Define method add that obtains another Fraction object named other as input and 
        # returns a new Fraction object representing the sum of itself and the input fraction. 
        # The resulting fraction should not be automatically simplified. 
        # For example, if the given fraction is 1/2 and the input argument is 3/4, 
        # the result will be 10/8 since numerator = 1*3 + 2*4,denominator = 2*4.
        
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        # Define method multiply that obtains another Fraction object named other as input and returns a new Fraction object representing the product of the two fractions. The resulting fraction should not be automatically simplified. For example, if the given fraction is 1/2 and the input argument is 3/4, the result will be 3/8 since
        # numerator = 1*3,denominator = 2*4.
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def gcd(self, a, b):
        # Part (c): Simplify the fraction
        # Define method gcd that takes two positive integers a, b as inputs and 
        # returns the greatest common divisor of a and b. 
        # For example, if two inputs are 16 and 20, the result will be 4.

        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        # Define method simplify in order to simplify the current Fraction class. F
        # or example, if the fraction number has __numerator=16 and __denomintator=20, the new numerator and denominator will be __numerator=4 and __denomintator=5 after calling this method.

        common = self.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

if __name__ == "__main__":
    # Input
    # The input has two lines:
    # The first line has two positive integers, separated by space, each ranges from 1 to 105, displaying the numerator and denominator of the first fraction.
    # The second line has two positive integers, separated by space, each ranges from 1 to 105, displaying the numerator and denominator of the second fraction.
    
    n1, d1 = map(int, input().split())
    frac1 = Fraction(n1, d1)
    
    n2, d2 = map(int, input().split())
    frac2 = Fraction(n2, d2)
    
    sum_frac = frac1.add(frac2)
    sum_frac.simplify()
    
    # Output
    # The output has two lines:
    # The first line shows the sum of two fractions in simplified form.
    # The second line shows the product of two fractions in simplified form.
    
    print(f"{sum_frac.numerator}/{sum_frac.denominator}")
    
    mult_frac = frac1.multiply(frac2)
    mult_frac.simplify()
    print(f"{mult_frac.numerator}/{mult_frac.denominator}")
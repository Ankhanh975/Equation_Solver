# B. My Rectangle is Bigger
# Define a Python class named Rectangle 
# initialized with two attributes, length and width:

class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        # Part (a): Defining methods
        # This class has the following components:
        # An __init__ function accepts two arguments: length and width. It assigns the values of these arguments to the instance variables length and width, respectively.
        
        self.length = length
        self.width = width

    def area(self) -> float:
        # An area method that calculates the area of the rectangle with formula length*width.
        return self.length * self.width

    def perimeter(self) -> float:
        # An perimeter method that calculates the perimeter with formula (length+width)*2.
        return 2 * (self.length + self.width)

    def __str__(self) -> str:
        # Part (b): Usage of built-in methods:
        # Extend the class Rectangle with three built-in methods:
        # A __str__ method returns the property of the rectangle, which is a string in the format:
        # "Rectangle(length=length_value, width=width_value)"
        # For example, if rec is an instance of Rectangle, you can simply run print(rec).
        
        return f"Rectangle(length={self.length}, width={self.width})"

    def __eq__(self, other):
        # An __eq__ method returns True if the areas of two rectangles are equal, otherwise False. For example, if rec1 and rec2 are two instances of Rectangle, you can check if these two objects are equal or not by running rec1 == rec2.
        return self.area() == other.area()

    def __lt__(self, other):
        # An __lt__ method returns True if the area of the first rectangle is smaller, otherwise False. For example, if rec1 and rec2 are two instances of Rectangle, you can check if the first object is less than the second object by running rec1 < rec2.
        return self.area() < other.area()


if __name__ == "__main__":
    # Input
    # The input has two lines:
    # Two positive integers display the length and width of the first rectangle, ranging from 1 to 1000 
    # Two positive integers display the length and width of the second rectangle, ranging from 1 to 1000 

    l1, w1 = map(int, input().split())
    rect1 = Rectangle(l1, w1)
    
    l2, w2 = map(int, input().split())
    rect2 = Rectangle(l2, w2)
    
    # Output
    # The input has five lines:
    # The first two lines show the properties of the two rectangles.
    # The third line shows the area of the first rectangle.
    # The fourth line shows the perimeter of the second rectangle.
    # The fifth line compares the first rectangle with the second one: bigger, smaller or equal.

    print(rect1)
    print(rect2)
    
    print(rect1.area())
    
    print(rect2.perimeter())
    
    if rect1 < rect2:
        print("smaller")
    elif rect1 > rect2:
        print("bigger")
    else:
        print("equal")
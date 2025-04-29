import math

def calculate_dist(xA: float, yA: float, xB: float, yB: float) -> float:
    """
    Return: float: The dist between A and B.
    """
    def square_difference(a: float, b: float):
        """
        Return: float: The square dist between A and B.
        """
        return (a - b) ** 2

    d = math.sqrt(square_difference(xA, xB) + square_difference(yA, yB))
    return round(d, 2)

if __name__ == "__main__":
    xA, yA = input().split(" ")
    xB, yB = input().split(" ")
    xA = float(xA)
    xB = float(xB)
    yA = float(yA)
    yB = float(yB)
    
    d = calculate_dist(xA, yA, xB, yB)
    print(f"{d:.2f}")
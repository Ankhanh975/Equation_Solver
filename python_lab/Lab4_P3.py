def calculate_area(length: float, width: float) -> float:
    assert length > 0, "Length must be positive."
    assert width > 0, "Width must be positive." 
    # Calculate the area of a rectangle in case inputs is valid.
    
    return int(length * width)

if __name__ == "__main__":
    length = float(input(""))
    width = float(input(""))
    print("Area:", calculate_area(length, width))   
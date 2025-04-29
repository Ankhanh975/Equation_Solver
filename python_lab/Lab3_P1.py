def rectangle_properties(length: int, width: int) -> tuple[int, int]:
    """
    Calculate the area and perimeter of a rectangle.
    """
    area = length * width
    perimeter =  2 * length + 2 * width
    return area, perimeter

if __name__ == "__main__":
    length, width = input().split(" ")
    length = int(length)
    width = int(width)
    
    area, perimeter = rectangle_properties(length, width)
    print(area, perimeter)
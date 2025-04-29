def convert_temperature(temp: float, unit: str = 'C') -> float:
    """
    Convert temp between Celsius and Fahrenheit.
    """
    if unit == 'C':
        converted = (temp * 9/5) + 32
    elif unit == 'F':
        converted = (temp - 32) * 5/9
    
    return round(converted, 2)

if __name__ == "__main__":
    i = input()
    temp = float(i)
    unit = input()
    converted_temp = convert_temperature(temp, unit)
    print(f"{converted_temp:.2f}")
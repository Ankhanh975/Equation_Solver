def solve(gears: list, direction) -> float:
    gear_check_point = gears.copy()
    
    while len(gears) >= 3:
        gears[1] *= gears[0] / gears[1]
        gears = gears[1:]
    
    final_ratio = 1
    # Get the direction
    if len(gear_check_point) % 2 == 0:
        final_ratio = final_ratio * (-1)
    if direction == "counter-clockwise":
       final_ratio = final_ratio * (-1)
            
    if len(gears) == 1:
        return final_ratio
    else:
        final_ratio *= gears[0] / gears[1]
        return final_ratio
    
if __name__ == "__main__":
    # gears = input()
    gears = "10 1 10"
    gears = gears.split(" ")
    for x in range(len(gears)):
        gears[x] = int(gears[x])
        
    print(solve(gears, "clockwise"))
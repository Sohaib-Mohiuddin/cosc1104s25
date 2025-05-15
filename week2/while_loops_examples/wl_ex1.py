# Example 1 - While Loops

units_to_ship = 20
truck_loads = 0
truck_capacity = 5

# while there are units to ship
while units_to_ship > 0:
    # load a truck
    truck_loads += 1
    
    # reduce the number of units to ship
    units_to_ship -= truck_capacity
    
# print the number of truck loads
print("Number of truck loads:", truck_loads)
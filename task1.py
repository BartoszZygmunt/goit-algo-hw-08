import heapq

def minimize_cable_cost_with_details(cable_lengths):
    """
    Given a list of cable lengths, this function computes the minimum total cost
    to connect all the cables into one single cable using the min-heap approach.
    The cost of connecting two cables is the sum of their lengths.
    
    The function uses a min-heap to always connect the two shortest cables first
    to minimize the total cost. It also prints the details of each connection step.
    
    """
    
    # Convert the list of cable lengths into a min-heap.
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    combinations = []  # To store details of the combinations made

    # Keep combining cables until only one cable remains in the heap
    while len(cable_lengths) > 1:
        # Extract the two shortest cables from the heap
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # The cost to combine these two cables is their sum
        combined_length = first + second
        total_cost += combined_length
        
        # Store the details of this combination
        combinations.append((first, second, combined_length))
        
        # Add the new combined cable back into the heap
        heapq.heappush(cable_lengths, combined_length)
    
    # Print the details of each combination
    print("Details of cable combinations:")
    for first, second, combined_length in combinations:
        print(f"Connected cables of lengths {first} and {second}, resulting in {combined_length}")
    
    # Print the minimum total cost to connect all cables
    print(f"\nMinimum total cost to connect all cables: {total_cost}")
    
    return total_cost



# Tests
cable_lengths1 = [8, 4, 6, 12]
cable_lengths2 = [1, 2, 3, 4]
cable_lengths3 = [5, 2, 8, 3, 7]

print("\nTest 1:")
minimize_cable_cost_with_details(cable_lengths1.copy())
print("\nTest 2:")
minimize_cable_cost_with_details(cable_lengths2.copy())
print("\nTest 3:")
minimize_cable_cost_with_details(cable_lengths3.copy())

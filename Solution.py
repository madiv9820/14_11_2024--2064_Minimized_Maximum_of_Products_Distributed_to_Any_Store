from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        # Helper function that checks if it's possible to distribute
        # the quantities into 'n' groups with each group having at most 'x' items.
        def canDistribute(x: int) -> bool:
            stores = 0
            # Calculate the total number of groups required if each group can hold at most 'x' items.
            # For each quantity 'q', we need ceil(q / x) groups, since each group can hold at most 'x' items.
            # If the sum of all the required groups is less than or equal to 'n', we can distribute.            
            for q in quantities:
                stores += math.ceil(q / x) # Add required stores for this quantity

            # If the total number of stores needed is less than or equal to `n`, it's a valid distribution
            return stores <= n
            
            # It can be done in one line in python
            # return sum(math.ceil(q / x) for q in quantities) <= n
        
        # Initialize 'ans' to 0, which will store the largest feasible value of 'x'.
        ans = 0
        
        # Start iterating over all possible values of 'x' from 'max(quantities)' down to 1.
        # This loop will find the largest 'x' such that the distribution is still possible.
        for x in range(max(quantities) + 1, 0, -1):  # Loop from max(quantities) to 1
            if canDistribute(x):  # Check if it's possible to distribute with 'x' items per group.
                ans = x  # If it's possible, set 'ans' to 'x'.
                
        # Return the largest feasible 'x' that allows a valid distribution.
        return ans
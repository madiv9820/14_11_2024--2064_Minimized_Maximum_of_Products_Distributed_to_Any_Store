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


        # Initialize binary search bounds
        min_x, max_x = 1, max(quantities)  # min_x starts at 1 (minimum items per store), max_x is the largest quantity
        
        # Variable to store the answer (the largest valid x)
        ans = 0

        # Perform binary search on the value of 'x'
        # We are searching for the largest possible 'x' where it's still possible to distribute the quantities.
        while min_x <= max_x:
            # Find the middle point of the current search range
            x = (min_x + max_x) // 2

            # Check if we can distribute the quantities such that no store has more than 'x' items
            if canDistribute(x):
                # If it's possible to distribute with 'x', it means we can try a larger 'x'
                # So, we update the answer and reduce the search range by setting max_x to x - 1
                ans = x
                max_x = x - 1
            else:
                # If it's not possible to distribute with 'x', we need to try a larger value of 'x'
                # So, we increase the search range by setting min_x to x + 1
                min_x = x + 1

        # Return the largest 'x' that allowed a valid distribution
        return ans
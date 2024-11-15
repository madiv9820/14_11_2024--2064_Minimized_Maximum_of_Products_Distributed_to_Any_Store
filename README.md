# Minimized Maximum of Products Distributed to Any Store (All Approaches)

- ## Approach 1:- Linear Search (Time Limit Exceeded)
    - ### Problem Understanding
        Given:
        - A list of item quantities.
        - An integer `n` representing the number of stores.

        The task is to find the largest `x` such that it is possible to distribute all the quantities into `n` stores, with no store holding more than `x` items. 

    - ### Intuition
        To solve this problem, we need to minimize the maximum number of items in any store while ensuring that all items are distributed into `n` stores or fewer. The key observation is:
            - For each possible `x`, we need to check if it's possible to distribute all the quantities into stores such that each store holds at most `x` items.
            - For a given `x`, the number of stores required for each quantity `q` is `ceil(q / x)`. This is because if we can only put `x` items in a store, we need to divide `q` by `x` and round up the result to account for partial stores.

    - ### Approach
        1. **Helper Function (`canDistribute`)**:
            - We will use a helper function to check if it's possible to distribute the quantities into `n` stores, where no store holds more than `x` items.
            - For each quantity `q`, calculate the number of stores needed: `ceil(q / x)`.
            - Sum the required stores and check if the total is less than or equal to `n`.
        2. **Search for Maximum `x`**:
            - We start from the largest possible value of `x` (i.e., `max(quantities)`) and decrement down to 1. This allows us to find the largest `x` that works.
            - The first valid `x` we find is the answer, since we are searching in descending order.

    - ### Code
        - **Python Code**

            ```python3 []
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
            ```

        - **C++ Solution**

            ```cpp []
            class Solution {
            public:
                int minimizedMaximum(int n, vector<int>& quantities) {
                    
                    // Lambda function to check if it's possible to distribute the quantities into `n` stores,
                    // where no store can have more than `x` items.
                    function<bool(int)> canDistribute = [&](int x) -> bool {
                        int stores = 0;
                        // For each quantity 'q' in the list of quantities, calculate how many stores are needed.
                        // We use ceil to round up the result of q / x (i.e., how many groups of size 'x' we need).
                        // `ceil(float(q) / x)` ensures that we round up the result to the nearest integer.
                        for (const int& q : quantities) {
                            stores += int(ceil(float(q) / x));  // Add required stores for this quantity
                        }
                        // If the total number of stores needed is less than or equal to `n`, it's a valid distribution
                        return stores <= n;
                    };

                    // The largest possible number of items in a store is `max(quantities)`.
                    int ans = 0;
                    
                    // Try every possible number of items per store `x` from `max(quantities)` down to 1
                    // We are looking for the largest `x` that satisfies the condition.
                    for (int x = *max_element(quantities.begin(), quantities.end()); x >= 1; --x) {
                        // If it's possible to distribute with `x` items per store, update the answer
                        if (canDistribute(x)) {
                            ans = x;  // Set the answer to the current value of x
                        }
                    }
                    
                    // Return the largest x that works, which minimizes the maximum items per store
                    return ans;
                }
            };
            ```

    - ### Time Complexity
        - **Helper Function (`canDistribute`)**:
            - The helper function loops through the `quantities` list and calculates the required stores for each quantity, which takes `O(m)` time, where `m` is the number of items in `quantities`.        
        - **Main Loop**:
            - The main loop runs from `max(quantities)` down to 1, which takes `O(max(quantities))` iterations in the worst case.
        - **Overall Time Complexity**:
            - `O(m * max(quantities))`, where `m` is the length of `quantities` and `max(quantities)` is the largest value in the `quantities` list.

    - ### Space Complexity
        - **Auxiliary Space**:
            - We only use a few integer variables and the input list `quantities`, so the space complexity is **O(1)** beyond the input storage.
        - **Overall Space Complexity**: **O(1)** (constant space).

- ## Approach 2:- Binary Search
    - ### Problem Intuition
        The problem asks us to distribute a list of quantities into `n` stores such that the maximum number of items in any store is minimized. The objective is to find the largest possible value `x` such that it is still possible to distribute all the quantities across `n` stores, with each store holding at most `x` items.

    - ### Key Observations:
        - **Distribute items efficiently**: For any given `x`, we need to determine if we can distribute the items such that no store holds more than `x` items.
        - **Calculating store requirements**: If `q` is the number of items for a certain quantity, the number of stores required to distribute `q` items with each store holding at most `x` items is `ceil(q / x)`. 
        - **Binary Search**: The problem becomes finding the largest possible value of `x` for which the distribution is still valid. We can efficiently perform this search using **binary search** because we are looking for the optimal value of `x` within a continuous range.

    - ### Approach
        1. **Helper Function `canDistribute(x)`**:
            - The helper function checks whether it is possible to distribute all quantities into `n` stores with each store holding at most `x` items.
            - For each quantity, we calculate the number of stores required, using the ceiling of the division of the quantity by `x`.
            - If the sum of required stores across all quantities is less than or equal to `n`, the function returns `True`. Otherwise, it returns `False`.

        2. **Binary Search**:
            - We use binary search on the possible values of `x` to find the largest `x` such that distribution is possible. The binary search range is between `1` (minimum possible number of items per store) and `max(quantities)` (the maximum possible number of items per store).
            - The binary search continues by adjusting the search range based on the result of the `canDistribute` function:
                - If distribution is possible with a given `x`, we search for potentially larger values of `x` by adjusting the lower bound (`min_x = x + 1`).
                - If distribution is not possible with a given `x`, we reduce the search space by adjusting the upper bound (`max_x = x - 1`).

        3. **Return Result**:
            - The binary search will converge to the largest feasible value of `x`, which is then returned as the answer.

    - ### Code
        - **Python Solution**

            ```python3 []
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
            ```

        - **C++ Solution**

            ```cpp []
            class Solution {
            public:
                int minimizedMaximum(int n, vector<int>& quantities) {
                    
                    // Helper function that checks if it's possible to distribute
                    // the quantities into 'n' groups with each group having at most 'x' items.
                    function<bool(int)> canDistribute = [&](int x) -> bool {
                        int stores = 0;
                        // Calculate the total number of groups required if each group can hold at most 'x' items.
                        // For each quantity 'q', we need ceil(q / x) groups, since each group can hold at most 'x' items.
                        // If the sum of all the required groups is less than or equal to 'n', we can distribute.
                        for (const int& q : quantities)
                            stores += int(ceil(float(q) / x));  // Add required stores for this quantity

                        // If the total number of stores needed is less than or equal to `n`, it's a valid distribution
                        return stores <= n;
                    };

                    // Initialize binary search bounds
                    int min_x = 1, max_x = *max_element(quantities.begin(), quantities.end());
                    
                    // Variable to store the answer (the largest valid x)
                    int ans = 0;

                    // Perform binary search on the value of 'x'
                    // We are searching for the largest possible 'x' where it's still possible to distribute the quantities.
                    while(min_x <= max_x) {
                        // Find the middle point of the current search range
                        int x = (max_x + min_x) / 2;
                        
                        // Check if we can distribute the quantities such that no store has more than 'x' items
                        if(canDistribute(x)) {
                            // If it's possible to distribute with 'x', it means we can try a larger 'x'
                            // So, we update the answer and reduce the search range by setting max_x to x - 1
                            ans = x;
                            max_x = x-1;
                        }
                        else {
                            // If it's not possible to distribute with 'x', we need to try a larger value of 'x'
                            // So, we increase the search range by setting min_x to x + 1
                            min_x = x+1;
                        }
                    }
                    
                    // Return the largest 'x' that allowed a valid distribution
                    return ans;
                }
            };
            ```

    - ### Time Complexity
        - **`canDistribute` Function**: This function iterates through the list of `quantities` and for each quantity, performs a ceiling operation. The time complexity of the `canDistribute` function is **O(m)**, where `m` is the number of quantities in the list.

        - **Binary Search**: The binary search is performed over the range from `1` to `max(quantities)`. The number of iterations in the binary search is **O(log(max(quantities)))**, as the search space is halved at each step.

        - **Total Time Complexity**: Since the binary search runs in **O(log(max(quantities)))** iterations and for each iteration, we call `canDistribute` which takes **O(m)** time, the total time complexity of the algorithm is: **O(m * log(max(quantities)))**

    - ### Space Complexity
        - **Auxiliary Space**: The algorithm uses only a few integer variables (`min_x`, `max_x`, `x`, `stores`, etc.) in addition to the input list `quantities`. There are no additional data structures that depend on the input size.

        - **Overall Space Complexity**: The space complexity is **O(1)** (constant space), excluding the input storage.
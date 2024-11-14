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
                int minimizedMaximum(int n, vector<int> quantities) {
                    
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
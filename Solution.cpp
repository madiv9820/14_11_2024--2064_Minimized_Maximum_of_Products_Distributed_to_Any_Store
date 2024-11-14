#include <iostream>
#include <vector>
#include <cmath>
#include <functional>
#include <algorithm>
using namespace std;

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

int main() {
    int n, input; vector<int> quantities; Solution sol;
    cin >> n >> input;

    while(input != -1) {
        quantities.emplace_back(input);
        cin >> input;
    }

    cout << sol.minimizedMaximum(n, quantities) << endl;
}
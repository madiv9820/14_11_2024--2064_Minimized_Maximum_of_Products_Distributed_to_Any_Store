#include <iostream>
#include <vector>
#include <functional>
#include <cmath>
#include <algorithm>
using namespace std;

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

int main() {
    int n, input; vector<int> quantities; Solution sol;
    cin >> n >> input;
    
    while(input != -1) {
        quantities.emplace_back(input);
        cin >> input;
    }

    cout << sol.minimizedMaximum(n, quantities) << endl;
}
# [2064. Minimized Maximum of Products Distributed to Any Store](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store)

__Type:__ Medium <br>
__Topics:__ Array, Binary Search <br>
__Companies:__ Amazon, Siemens, Google, Bloomberg, Flipkart
<hr>

You are given an integer `n` indicating there are `n` specialty retail stores. There are `m` product types of varying amounts, which are given as a __0-indexed__ integer array `quantities`, where `quantities[i]` represents the number of products of the <code>i<sup>th</sup></code> product type.

You need to distribute __all products__ to the retail stores following these rules:
- A store can only be given __at most one product type__ but can be given __any__ amount of it.
- After distribution, each store will have been given some number of products (possibly `0`). Let `x` represent the maximum number of products given to any store. You want `x` to be as small as possible, i.e., you want to __minimize__ the __maximum__ number of products that are given to any store.

Return _the minimum possible_ `x`.
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ n = 6, quantities = [11,6] <br>
__Output:__ 3 <br>
__Explanation:__ One optimal way is: <br> - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3 <br> - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3 <br> The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

- __Example 2:__ <br>
__Input:__ n = 7, quantities = [15,10,10] <br>
__Output:__ 5 <br>
__Explanation:__ One optimal way is: <br> - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5 <br> - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5 <br> - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5 <br> The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.

- __Example 3:__ <br>
__Input:__ n = 1, quantities = [100000] <br>
__Output:__ 100000 <br>
__Explanation:__ The only optimal way is: <br> - The 100000 products of type 0 are distributed to the only store. <br> The maximum number of products given to any store is max(100000) = 100000.
<hr>

### Constraints:

- `m == quantities.length`
- <code>1 <= m <= n <= 10<sup>5</sup></code>
- <code>1 <= quantities[i] <= 10<sup>5</sup></code>
<hr>

### Hints:
- There exists a monotonic nature such that when x is smaller than some number, there will be no way to distribute, and when x is not smaller than that number, there will always be a way to distribute.
- If you are given a number k, where the number of products given to any store does not exceed k, could you determine if all products can be distributed?
- Implement a function canDistribute(k), which returns true if you can distribute all products such that any store will not be given more than k products, and returns false if you cannot. Use this function to binary search for the smallest possible k.
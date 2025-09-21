## 1.Two Sum
### Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#### Solution
Using list, two **for loops** will add up two adjacent elements and compare the result with a given target

### Better Approach
Using a **hash table**

#### What is hash table?
Hash table is a kind of data structure to store KV(key-value). This makes searching way more faster.

Anyway, first, store an element with its index. Second, substract the element from target value(find *complement*) and finally, check if the complement is at the given list.
If there is no complement, store the current number with its index in the hash table.

### Comparison
#### My solution
- Time complexity:O(n^2)
- Space complexity:O(1)
#### Better Approach
- Time complexity:O(n)
- Space complexity:O(n)


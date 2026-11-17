"""
LeetCode 1. Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Approach: Hash Map (One-pass)
Instead of using a nested loop, we can use a hash map to store the numbers we have seen so far. 
For each number, we calculate its complement (target - num) and check if it's in the hash map.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(n) - In the worst case, we store all elements in the hash map.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #哈希表
        hash={}
        for i,v in enumerate(nums):
            prev=target-v
            if prev in hash:
              return[hash[prev],i]
            hash[v]=i
        return []

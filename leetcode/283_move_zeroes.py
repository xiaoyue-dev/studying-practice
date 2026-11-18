"""
LeetCode 283. Move Zeroes
Difficulty: Easy
Link: https://leetcode.com/problems/move-zeroes/

Approach: Two Pointers (Fast and Slow)
We use a fast pointer to iterate through the array, and a slow pointer to track the position of the next non-zero element. 
When the fast pointer finds a non-zero element, we swap it with the element at the slow pointer, and increment the slow pointer.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(1) - We modify the array in-place without extra space.
"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
                

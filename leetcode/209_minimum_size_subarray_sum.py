"""
LeetCode 209. Minimum Size Subarray Sum
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Approach: Sliding Window (Two Pointers)
We use a sliding window defined by `start` and `end`. 
We expand the window by moving `end` and adding elements to `total`. 
When `total >= target`, we update the minimum length, and then shrink the window from the left by moving `start` and subtracting `nums[start]` from `total` until the condition is no longer met.

Time Complexity: O(n) - Each element is added to the window once and removed once.
Space Complexity: O(1) - Only a few variables are used.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        ans = n + 1  # Initialize with a value larger than any possible valid length
        start = 0
        total = 0
        
        # Expand the window to the right
        for end in range(n):
            total += nums[end]
            
            # Shrink the window from the left while the condition is met
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
                
        # If ans is still n + 1, it means no valid subarray was found
        return 0 if ans == n + 1 else ans

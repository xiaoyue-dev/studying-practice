"""
LeetCode 53. Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Approach: Dynamic Programming (Kadane's Algorithm - In-place)
We iterate through the array. If the previous element (which represents the max sum ending at the previous index) is greater than 0, it contributes positively to the current sum. We add it to the current element.
Otherwise, we start a new subarray from the current element. Finally, the maximum value in the modified array is our answer.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(1) - We modify the array in-place.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            # If the previous cumulative sum is positive, add it to the current number
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                
        # The maximum value in the modified array is the max subarray sum
        return max(nums)

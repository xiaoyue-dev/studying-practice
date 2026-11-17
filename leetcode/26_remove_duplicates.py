"""
LeetCode 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach: Two Pointers (Fast and Slow)
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        slow=0
        for fast in range(1,len(nums)):
            if  nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        return slow+1

"""
LeetCode 88. Merge Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/merge-sorted-array/

Approach: Two Pointers (From the end)
Since nums1 has enough empty space at the end, we can use three pointers starting from the back. 
Compare the largest elements of nums1 and nums2, and place the larger one at the end of nums1.

Time Complexity: O(m + n) - We traverse both arrays at most once.
Space Complexity: O(1) - We modify nums1 in-place without extra space.
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = len(nums1) - 1
        i1 = m - 1
        i2 = n - 1
        while True:
            if i1 == -1 and i2 == -1:
                break
            elif i1 == -1:
                nums1[tail] = nums2[i2]
                i2 -= 1
            elif i2 == -1:
                nums1[tail] = nums1[i1]
                i1 -= 1
            else:
                if nums1[i1] > nums2[i2]:
                    nums1[tail] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[tail] = nums2[i2]
                    i2 -= 1
            tail -= 1

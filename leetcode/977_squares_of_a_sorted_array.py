"""
LeetCode 977. Squares of a Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Approach: Two Pointers (From both ends)
Since the array is sorted, the maximum square value must come from either the most negative number (at the beginning) or the most positive number (at the end). 
We use two pointers starting from both ends, compare their squares, and place the larger one at the end of the result array.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(n) - We need an extra array to store the result.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        head=0
        tail=n-1
        curr=n-1
        while curr>=0:
            head_square=nums[head]*nums[head]
            tail_square=nums[tail]*nums[tail]
            if(head_square>=tail_square):
                ans[curr]=head_square
                head+=1
            else:
                ans[curr]=tail_square
                tail-=1
            curr-=1
        return ans

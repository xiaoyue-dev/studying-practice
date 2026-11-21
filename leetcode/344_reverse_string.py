"""
LeetCode 344. Reverse String
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string/

Approach: Two Pointers (Head and Tail)
Use two pointers, one at the beginning and one at the end of the string. 
Swap the characters they point to, then move the head pointer forward and the tail pointer backward. 
Repeat until the two pointers meet.

Time Complexity: O(n) - We iterate through half of the array.
Space Complexity: O(1) - We modify the array in-place with constant extra space.
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s) - 1
        
        # Swap characters from both ends towards the middle
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1

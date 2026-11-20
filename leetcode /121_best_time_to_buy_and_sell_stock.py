"""
LeetCode 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach: One-pass (Dynamic Programming / Greedy)
Iterate through the prices once. Maintain the minimum price seen so far and the maximum profit. 
For each price, update the minimum price first, and then calculate the potential profit if we sell today to update the maximum profit.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(1) - Only two variables are used.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize minimum price to positive infinity
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price seen so far
            min_price = min(price, min_price)
            # Calculate the profit and update the maximum profit
            max_profit = max(max_profit, price - min_price)
            
        return max_profit

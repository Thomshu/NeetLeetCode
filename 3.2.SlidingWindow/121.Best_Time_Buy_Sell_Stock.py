'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #Sliding window technique, reducing a double for loop to a single for loop using two pointers
        left = 0
        right = 1
        maxprof = 0

        # The alternative (bad way) where you run into time exceeded is to do two for loops
        #Better way below is sliding window technique
        while right < len(prices):
            if prices[left] < prices[right]:
                difference = prices[right]-prices[left]
                if (maxprof < difference):
                    maxprof = difference

            else: #This is the case where the left price is NOT smaller than the right price, thus left price will always be less max profit then the right price
                # In this case, we simply just assign the left pointer to the right pointer item and keep finding max profits from there
                left = right
            
            right = right+1 #keep sliding the pointer to the right
        return maxprof
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

Logic: Sliding window. We care about 2 things: 1. Is this the smallest buy in value? 2. Is this the best profit?
Time: O(n)
Space: O(1)
'''



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]         # start with first price as buy
        max_profit = 0          # 0 because no transaction = 0 profit

        for sell in range(1, len(prices)):
            if prices[sell] < buy:
                buy = prices[sell]  # found cheaper price, update buy point
            else:
                max_profit = max(max_profit, prices[sell] - buy)  # is this our best profit?

        return max_profit
    
if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([3,1,7,2,4]) == 6
    assert sol.maxProfit([0,0,0,0,0]) == 0
    print("All tests passed!")

    
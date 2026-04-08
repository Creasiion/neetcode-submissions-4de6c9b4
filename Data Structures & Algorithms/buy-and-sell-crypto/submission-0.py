class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 #Index of what day we want to buy
        sell = 1 #Index of what day we want to sell
        maxProfit = 0
        while sell < len(prices):
            if(prices[buy] < prices[sell]):
                curr = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, curr)
            else: #A smaller buying price has been found
                buy = sell
            sell += 1
        return maxProfit


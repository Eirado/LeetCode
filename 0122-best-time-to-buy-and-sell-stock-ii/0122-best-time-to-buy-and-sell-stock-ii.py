class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] > prices[i + 1]:
                i += 1
            buy = prices[i]

            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
            profit += prices[i] - buy
            i += 1
        return profit

    # Two moments, lowest moment, highest moment
    # lowest moment buy 
    # highest moment sell
    # [7,1,5,3,6,4]
        
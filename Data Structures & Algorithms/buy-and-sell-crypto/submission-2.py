class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxprofit = 0
        for j in range(1, len(prices)):
            if prices[i] < prices[j]:
                maxprofit = max(maxprofit, (prices[j] - prices[i]))
            else:
                i = j
        return maxprofit
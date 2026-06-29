class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       i, j = 0, 1
       mxprofit = 0

       while j < len(prices):
        if prices[i]<prices[j]:
            profit = prices[j] - prices[i]
            mxprofit = max(mxprofit,profit)
        else:
            i=j
        j+=1
       return mxprofit
       
        
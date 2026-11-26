class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                k = prices[j] - prices[i]
                print(k)
                profit= max(profit,k)
        return profit



        
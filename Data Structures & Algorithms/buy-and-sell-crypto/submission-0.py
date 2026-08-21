class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        l = 0

        for r in range(1, len(prices)):
            while (prices[r] - prices[l]) < 0:
                l += 1
            if (prices[r] - prices[l]) > best_profit:
                best_profit = (prices[r] - prices[l])
        
        return best_profit
            


        
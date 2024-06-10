class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        cp = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < cp :
                cp = prices[i]
            elif prices[i] - cp > mp :
                mp = prices[i] - cp
        return mp

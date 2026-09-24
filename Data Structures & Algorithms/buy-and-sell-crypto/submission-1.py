class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        PL=0
        buy=prices[0]
        for i in range(len(prices)) :
            buy=min(buy,prices[i])
            PL=max(0,PL,prices[i]-buy)
        
        return PL
        
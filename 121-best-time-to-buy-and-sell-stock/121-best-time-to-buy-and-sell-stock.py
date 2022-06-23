class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Cache smallest we've seen so far
        # Find the max in future 
        
        curLow = float("inf")
        maxProfit = 0
        
        for p in prices:
            maxProfit = max(maxProfit, p - curLow)
            curLow = min(p, curLow)
        return maxProfit
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dp = defaultdict(list)
        minLen = float("inf")
        maxDeg = -float("inf")

        
        for i, n in enumerate(nums):
            dp[n].append(i)
            
            if len(dp[n]) > maxDeg:
                maxDeg = len(dp[n])
                minLen = dp[n][-1] - dp[n][0] + 1
            elif len(dp[n]) == maxDeg:
                minLen = min(minLen, dp[n][-1] - dp[n][0] + 1)
        
        return minLen
        
        
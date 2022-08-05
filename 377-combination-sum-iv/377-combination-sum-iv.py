class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        dp = {}
        
        
        
        
        def dfs(curSum=0):
            if curSum > target:
                return 0 # This is not a valid solution 
            elif curSum == target:
                return 1 # valid
            if curSum in dp:
                return dp[curSum]
            
            tmpSum = 0
            
            # add ALL children
            for n in nums:
                if curSum + n <= target:
                    tmpSum += dfs(curSum + n)
            
            dp[curSum] = tmpSum
            
            return tmpSum
        

        
        
        return dfs()
        
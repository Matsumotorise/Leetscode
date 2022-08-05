class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        
        @lru_cache(maxsize=100000)
        def dfs(curSum=0):
            if curSum > target:
                return 0 # This is not a valid solution 
            elif curSum == target:
                return 1 # valid
            
            tmpSum = 0
            
            # add ALL children
            for n in nums:
                if curSum + n <= target:
                    tmpSum += dfs(curSum + n)
            
            return tmpSum
        

        
        
        return dfs()
        
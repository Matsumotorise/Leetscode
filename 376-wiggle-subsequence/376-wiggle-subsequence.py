class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        # lastPosLIS, lastNegLIS, posnegFlag
        dp = [(1, 1, 0)] * len(nums)
        dp[-1] = (1, 1, 0x11)
        maxSz = 1
        
        for i in range(len(nums)-2, -1, -1):
            
            maxLISPos = 1
            maxLISNeg = 1
            curFlag = 0
            for j in range(i, len(nums)):
                pLIS, nLIS, flag = dp[j]
                # if it qualifies to interact with ours
                dy = nums[j] - nums[i] # deriv
                if dy == 0:
                    continue
                if flag & 0x01 and dy < 0:
                    curFlag |= 0x1
                    maxLISNeg = max(maxLISNeg, pLIS + 1)
                elif flag & 0x1 and dy > 0:
                    curFlag |= 0x01
                    maxLISPos = max(maxLISPos, nLIS + 1)
                
            maxSz = max(maxSz, maxLISNeg, maxLISPos)
            dp[i] = (maxLISPos, maxLISNeg, curFlag)
                
        return maxSz
                
                
                
            
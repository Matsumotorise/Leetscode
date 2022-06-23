# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        leftMostBadVersion = float('inf')
        while l <= r:
            mid = (l+r) // 2
            
            # Look left if necessary
            if isBadVersion(mid):
                leftMostBadVersion = min(mid, leftMostBadVersion)
                r = mid - 1
            # Look right if necessary
            else:
                l = mid + 1
                
        
        return leftMostBadVersion
        # [1,2,3,4,5] 4 is bad
        #      m
        #        l r
        #        m 

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        
        for i in range(n+1):
            count = 0
            while i > 0:
                count += i & 0x1
                i >>= 1
            res.append(count)
            
        return res 
            
        
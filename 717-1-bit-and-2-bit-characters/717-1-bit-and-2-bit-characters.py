class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        n = len(bits)
        i = 0
        while i < len(bits):
            if i == n-1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return False
                
        
        
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1)-1
        s1Counter = Counter(s1)
        s2Counter = Counter(s2[l:r+1])
        
        while r < len(s2):
            
            # compare if it is a permutation
            if s1Counter == s2Counter:
                return True
            
            # update the counter
            s2Counter[s2[l]] -= 1
            if s2Counter[s2[l]] == 0:
                del s2Counter[s2[l]]
            if r+1 < len(s2):
                s2Counter[s2[r+1]] +=1
                
            l += 1
            r += 1
            
            
        return False
        
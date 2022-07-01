class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        
        numDiff = 0
        
        fMapS, fMapT = Counter(s), Counter(t)
        
        for k, v in fMapS.items():
            numDiff += max(0,v - fMapT[k])
                
        return numDiff
        
        
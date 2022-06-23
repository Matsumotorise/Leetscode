class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        targetMap = Counter(ransomNote)
        letterMap = Counter(magazine)
        
        for k, v in targetMap.items():
            if k in letterMap:
                if letterMap[k] < v:
                    return False
            else:
                return False
            
        return True
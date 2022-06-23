class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        map1, map2 = Counter(s), Counter(t)
        return map1 == map2
        
        
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = collections.Counter(s) # O(n) space, time
        tCounter = collections.Counter(t) # O(n) space, time
        return sCounter == tCounter # O(n) time, no additional space
        
        
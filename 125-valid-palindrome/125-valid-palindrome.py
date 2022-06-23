class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = "".join("" if not x.isalpha() and not x.isdigit() else x for x in s)
        
        return s == s[::-1]
        
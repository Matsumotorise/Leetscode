class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        data = "".join(s.split("-"))[::-1]
        
        ret = []
        for i in range(0, len(data), k):
            ret.append(data[i:i+k].upper()[::-1])
            
        return "-".join(ret[::-1])
        
        
        
        
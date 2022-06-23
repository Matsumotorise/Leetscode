class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if a == "0" and b == "0":
            return "0"
        
        carry = 0
        p1, p2 = len(a)-1, len(b)-1
        
        from collections import deque
        
        res = deque([])
        
        while carry != 0 or p1 >= 0 or p2>=0:
            tmp = 0
            if carry:
                tmp += 1
            if p1 >= 0 and a[p1] == "1":
                tmp += 1
            if p2 >= 0 and b[p2] == "1":
                tmp += 1
            
            res.appendleft(str(tmp % 2))
            carry = tmp // 2
            p1 -= 1
            p2 -= 1
        
        return "".join(res)
        
        
        
        
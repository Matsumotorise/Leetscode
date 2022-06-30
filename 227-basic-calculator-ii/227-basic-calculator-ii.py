class Solution:
    
    def calculate(self, s: str) -> int:
        stack = []
        
        curI = 0
        lastSymI = 0
        
        # Find first digit
        for i, x in enumerate(s):
            if x in ("*", "/", "+", "-"):
                curI = i+1
                lastSymI = i
                stack.append(int(s[:i]))
                break
        
        if curI == 0:
            return int(s)
        
        
        while curI < len(s):
            x = s[curI]
            if x in ("*", "/", "+", "-"):
                if s[lastSymI] == "*":
                    stack[-1] *= int(s[lastSymI+1:curI])
                elif s[lastSymI] == "/":
                    stack[-1] = int(stack[-1] / int(s[lastSymI+1:curI]))
                elif s[lastSymI] == "+":
                    stack.append(int(s[lastSymI+1:curI]))
                elif s[lastSymI] == "-":
                    stack.append(-int(s[lastSymI+1:curI]))
                lastSymI = curI
            curI+=1
            
        # do it for the last integer
        if s[lastSymI] == "*":
            stack[-1] *= int(s[lastSymI+1:curI])
        elif s[lastSymI] == "/":
            stack[-1] = int(stack[-1] / int(s[lastSymI+1:curI]))
        elif s[lastSymI] == "+":
            stack.append(int(s[lastSymI+1:curI]))
        elif s[lastSymI] == "-":
            stack.append(-int(s[lastSymI+1:curI]))

        
            
        return sum(stack)
            
            
            
            
            
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:
            # 5 cases, numerical, or symbol
            
            if t == "+": # add the previous 2 elements
                r = stack.pop()
                l = stack.pop()
                stack.append(l + r)
            elif t == "-": # subtract 2 prev elements
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)
            elif t == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(l * r)
            elif t == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r))
            else: # numerical
                stack.append(int(t))
            
        return stack[0]
            
            
        
        
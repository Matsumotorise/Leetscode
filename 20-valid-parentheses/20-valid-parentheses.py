class Solution:
    def isValid(self, s: str) -> bool:
        openMap = {"(": ")", "{":"}", "[":"]"}
        closeMap = {v:k for k,v in openMap.items()}
        
        
        
        stack = []
        
        for st in s:
            # 2 cases
            if st in openMap: # If it is an opening sequence
                stack.append(st)
            else: # If it is a closing sequence
                if len(stack) == 0 or closeMap[st] != stack.pop():
                    return False
                
        return len(stack) == 0
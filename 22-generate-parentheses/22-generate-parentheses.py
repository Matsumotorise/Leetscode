class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        curStr = []
        
        
        def dfs(numOpen=0, numClose=0):
            # Base case
            if numClose == n:
                lst.append("".join(curStr))
                
            # add children
            if numOpen < n:
                curStr.append("(")
                dfs(numOpen+1, numClose)
                curStr.pop()
            if numOpen > numClose:
                curStr.append(")")
                dfs(numOpen, numClose+1)
                curStr.pop()

        dfs()
        
        return lst
                
            
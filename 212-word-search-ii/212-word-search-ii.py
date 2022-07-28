class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.end = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        for word in words:
            self.root.addWord(word)
            
        nRows = len(board)
        nCols = len(board[0])
        
        
        res = []
        def dfs(r, c, curNode):
            # exit conditions
            curNode = curNode.children[board[r][c]]
            tmp = board[r][c]
            board[r][c] = "*"
            if curNode.end:
                res.append(curNode.end)
                curNode.end = False
            
            for nr, nc in ((r+1,c), (r-1,c), (r,c-1), (r,c+1)):
                if ((0 <= nr < nRows and 0 <= nc < nCols) and
                        board[nr][nc] in curNode.children):
                    dfs(nr,nc,curNode)
                
            board[r][c] = tmp
        
        for i in range(nRows):
            for j in range(nCols):
                dfs(i,j,self.root)
                
        return res
                
                
        

                
        
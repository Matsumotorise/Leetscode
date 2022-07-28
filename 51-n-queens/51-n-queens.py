class Solution:
    import copy
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.curSol = [["." for _ in range(n)] for _ in range(n)]
        self.sols = []
        
        negDiag = [0]*(2*n - 1)
        posDiag = [0]*(2*n - 1) 
        horiz = [0]*n
        
        def dfs(cn=0):
            if cn == n:
                self.sols.append(["".join(row) for row in self.curSol])
                return True
            
            # Find possible moves
            # We populate left to right, so cIdx = cn
            c = cn 
            for r in range(n): 
                # If it can satisfy not bumping into any other queen
                ndIdx = n+c-r-1
                psIdx = r+c
                if negDiag[ndIdx] == 0 and posDiag[psIdx] == 0 and horiz[r] == 0:
                    negDiag[ndIdx] += 1
                    posDiag[psIdx] += 1
                    horiz[r] += 1
                    self.curSol[r][c] = "Q"
                    dfs(cn+1)
                    self.curSol[r][c] = "."
                    negDiag[ndIdx] -= 1
                    posDiag[psIdx] -= 1
                    horiz[r] -= 1
                    
                    
        dfs(cn=0)
        return self.sols
        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        # go top down then left to right
        
        
        
        # top left edge case
        rowFlag =  any(x == 0 for x in matrix[0])
        colFlag =  any(x[0] == 0 for x in matrix) 
        
        nRows, nCols = len(matrix), len(matrix[0])
        
        for r in range(nRows):
            for c in range(nCols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        # next step wipe out
        
        for r in range(1,nRows):
            for c in range(1,nCols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                        
        
        if rowFlag:
            for i in range(nCols):
                matrix[0][i] = 0
            
        if colFlag:
            for i in range(nRows):
                matrix[i][0] = 0
        
        
        
        
        
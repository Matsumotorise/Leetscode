class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        nRows = len(grid)
        nCols = len(grid[0])
        numOranges = sum(1 for row in grid for f in row if f in (1,2))
        numRotten = sum(1 for row in grid for f in row if f ==2 )
        
        queue = deque([(r,c, 0) for r in range(nRows) for c in range(nCols) if grid[r][c] ==2])
        maxTime = 0

        while queue:
            r,c,d = queue.popleft()
            
            # do stuff
            maxTime = max(maxTime, d)
            
            # add children
            for nr,nc in ((r,c+1),(r,c-1),(r+1, c),(r-1, c)):
                if (0<=nr<nRows and 0<=nc<nCols) and grid[nr][nc] == 1:# can infect do it
                    grid[nr][nc] = 2
                    numRotten += 1
                    queue.append((nr,nc,d+1))
        
        
        return maxTime if numOranges == numRotten else -1
        
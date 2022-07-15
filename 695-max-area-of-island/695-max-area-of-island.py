class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        
        nRows, nCols = len(grid), len(grid[0])
        
        for rI in range(nRows):
            for cI in range(nCols):
                # If we need to visit this
                if grid[rI][cI] == 1:
                    # init stack
                    stack = [(rI,cI)]
                    grid[rI][cI] = 0
                    islandSz = 0
                    while stack:
                        r,c = stack.pop()
                        islandSz += 1
                        
                        # Append valid children
                        for nr, nc in ((r+1,c),(r-1,c),(r, c+1),(r, c-1)):
                            if 0<=nr<nRows and 0<=nc<nCols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                stack.append((nr,nc))
                        
                    maxArea = max(maxArea,islandSz)
        
        
        return maxArea
        
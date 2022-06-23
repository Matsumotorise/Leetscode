class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        nRows, nCols = len(image), len(image[0])
        
        stack = [(sr,sc)] 
        visited = set()
        startingColor = image[sr][sc]
        
        while stack:
            r,c = stack.pop()
            
            # exit conditions
            # invalid cord (OOB), In visited
            if (r,c) in visited:
                continue
                
            visited.add((r,c))
            image[r][c] = color
            
            for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r, c-1)):
                if 0 <= nr < nRows and 0 <= nc < nCols and image[nr][nc] == startingColor:
                    stack.append((nr,nc))
            
        return image
        
        
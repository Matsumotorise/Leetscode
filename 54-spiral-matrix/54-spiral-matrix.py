class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        nRows, nCols = len(matrix), len(matrix[0])
        
        stack = [(0,0)]
        toRet = []
        direction = "E"
        
        while stack:
            r,c = stack.pop()
            
            if (r,c) in visited or not (0<= r < nRows and 0 <= c < nCols):
                return toRet
            
            visited.add((r,c))
            toRet.append(matrix[r][c])
            
            # find next child
            if direction == "E":
                # if we hit a wall turn down
                if c == nCols-1 or (r,c+1) in visited:
                    direction = "S"
                    stack.append((r+1,c))
                else:
                    stack.append((r,c+1))
            elif direction == "S":
                # if we hit a wall turn west
                if r == nRows-1 or (r+1,c) in visited:
                    direction = "W"
                    stack.append((r,c-1))
                else:
                    stack.append((r+1,c))
            elif direction == "W":
                # if we hit a wall turn North
                if c == 0 or (r,c-1) in visited:
                    direction = "N"
                    stack.append((r-1,c))
                else:
                    stack.append((r,c-1))
            else: # N
                # if we hit a wall turn North
                if r == 0 or (r-1,c) in visited:
                    direction = "E"
                    stack.append((r,c+1))
                else:
                    stack.append((r-1,c))
            
            
            
        
        
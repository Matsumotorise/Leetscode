class Solution:
    from functools import lru_cache
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # my indexing scheme for 3x3 blocks
        def indexToSquareIndex(r, c):
            return (r//3) * 3 + (c//3)
        
        # Game play/TODO:
        # Keep hashmaps of the 9 larger squares
        # Keep hm of the individual Rows
        # Keep hm of the individual Cols
        # Update when doing DFS
        
        # The hms tell us of potential candidates for each slot.
        
        toVisit = set()
        validNums = Counter(i for i in range(1,10))
        squareCounter = [Counter() for _ in range(9)]
        rowHM = []
        colHM = []
        
        for i in range(9):
            colCntr = Counter()
            rowCntr = Counter()
            for j in range(9):
                colCntr[board[j][i]] += 1
                rowCntr[board[i][j]] += 1
                sIndex = indexToSquareIndex(i,j)
                squareCounter[sIndex][board[i][j]] += 1
                # Check board validity incase there's multiple numbers already violating
                if board[i][j] != "." and (squareCounter[sIndex][board[i][j]] > 1 or rowCntr[board[i][j]] > 1):
                    return False
                elif board[j][i] != "." and colCntr[board[j][i]] > 1:
                    return False
                elif board[i][j] == ".":
                    toVisit.add((i,j))
            rowHM.append(rowCntr)
            colHM.append(colCntr)
            
        
        return True
        
        '''
        print(validNums)
        print(squareCounter)
        print()
        print(rowHM)
        print()
        print(colHM)
        '''
        
        
        

        
        # Game plan, explore every possible "route". with dfs
        # Known dead-end routes are prohibitted via memoization
        visited = {}
        def dfs(r, c):
            # Counter of all possible actions at this position
            possibilities = validNums - squareCounter(indexToSquareIndex(r, c)) - rowHM[r] - colHM[c]
            
            # Exit conditions
            if len(toVisit) == 0 and len(possibilities) == 1:
                return True
            
            # Replace (r,c) with some action
            for candidateNum in possibilities: 
                squareIndex = indexToSquareIndex(r,c)
                # Check if it satisfies all constraints
                if candidateNum not in squareCounter[squareIndex] and num not in rowHM[r] and num not in colHM[c]: 
                    # Update for backtracking
                    squareCounter[squareIndex][candidateNum] += 1
                    rowHM[r][candidateNum] += 1
                    colHM[c][candidateNum] += 1
                    toVisit.remove((r, c))
                    for nr, nc in toVisit:
                        if dfs(nr, nc):
                            return True
                    toVisit.add((r, c))
                    del squareCounter[squareIndex][candidateNum]
                    del rowHM[r][candidateNum]
                    del colHM[c][candidateNum]
                   
            
            return False
                
        # Now for each "." @ (r, c) , we want to enumerate all possible ints that could go at (r,c)
        for r,c in toVisit:
            print(r,c)
            if dfs(r,c):
                return True

        
        
        return False
        
        
        
        
        
        
        
        
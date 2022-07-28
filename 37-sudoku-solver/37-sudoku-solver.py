class Solution:
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        # my indexing scheme for 3x3 blocks
        def indexToSquareIndex(r, c):
            return (r//3) * 3 + (c//3)
        
        # Game play/TODO:
        # Keep hashmaps of the 9 larger squares
        # Keep hm of the individual Rows
        # Keep hm of the individual Cols
        # Update when doing DFS
        
        # The hms tell us of potential candidates for each slot.
        
        toVisit = []
        validNums = Counter(str(i) for i in range(1,10))
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
                if board[i][j] == ".":
                    toVisit.append((i,j))
            rowHM.append(rowCntr)
            colHM.append(colCntr)
        
        
        '''
        print(validNums)
        print(squareCounter)
        print()
        print(rowHM)
        print()
        print(colHM)
        '''
        
        
        # Known list of options avalabile
        # 
        
        def dfs():
            # Counter of all possible actions at this position
            
            # Exit conditions
            if len(toVisit) == 0:
                return True
            
            r, c = toVisit.pop()
            
            squareIndex = indexToSquareIndex(r,c)
            
            # Replace (r,c) with some action
            for candidateNum in validNums: 
                if candidateNum not in squareCounter[squareIndex] and candidateNum not in rowHM[r] and candidateNum not in colHM[c]:
                    # Update for backtracking
                    squareCounter[squareIndex][candidateNum] += 1
                    rowHM[r][candidateNum] += 1
                    colHM[c][candidateNum] += 1
                    board[r][c] = candidateNum
                    if dfs():
                        return True
                    board[r][c] = "."
                    del squareCounter[squareIndex][candidateNum]
                    del rowHM[r][candidateNum]
                    del colHM[c][candidateNum]
                    
            toVisit.append((r,c))

            return False
                
        # Now for each "." @ (r, c) , we want to enumerate all possible ints that could go at (r,c)
        dfs()
        
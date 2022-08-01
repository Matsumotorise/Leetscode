from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        neighborMap = defaultdict(set)
        
        for i, row in enumerate(isConnected):
            for j, n in enumerate(row):
                if i != j and n == 1:
                    neighborMap[i].add(j)
        
        numProv = 0
        visited = set()
        
        def dfs(i):
            # add children and remove their edges
            while neighborMap[i]:
                child = neighborMap[i].pop()
                neighborMap[child].remove(i)
                visited.add(child)
                visited.add(i)
                dfs(child)
            
        
        for i, row in enumerate(isConnected):
            if i not in visited:
                dfs(i)
                numProv += 1
        return numProv
        
        
        
        

                
            
            
        

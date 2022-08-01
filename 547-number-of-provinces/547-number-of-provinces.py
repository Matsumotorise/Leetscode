from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        neighborMap = defaultdict(set)
        
        for i, row in enumerate(isConnected):
            for j, n in enumerate(row):
                if i != j and n == 1:
                    neighborMap[i].add(j)
        

        queue = deque([])
        visited = set()
        numProv = 0
        
        # Plan: BFS on each potential island
        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            numProv += 1
        
            queue = deque([i])
            while queue:
                curNode = queue.pop()
                
                # Exit conditions:
                if curNode in visited:
                    continue
                    
                visited.add(curNode)
                
                # Children
                
                while neighborMap[curNode]:
                    child = neighborMap[curNode].pop()
                    neighborMap[child].remove(curNode)
                    queue.appendleft(child)
            

        return numProv
                
            
            
        

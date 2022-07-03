class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs this path
        from collections import deque
        queue = deque([start])
        visited = set()
        
        while queue:
            idx = queue.popleft()
            # exit conds
            if arr[idx] == 0:
                return True
            
            visited.add(idx)
            
            # add children
            for ci in (idx+arr[idx], idx - arr[idx]):
                if 0 <= ci < len(arr) and ci not in visited: # if in bounds
                    queue.append(ci)
                    
            
            
        return False
                
            
            
        
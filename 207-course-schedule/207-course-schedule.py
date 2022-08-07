class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dest, src where src is a prereq
        # edges map 
        edges = defaultdict(list)
        
        for val, preq in prerequisites:
            edges[val].append(preq)
            
        print(edges)
        # We'll see using dfs if all of them the numCourses are valid:
        
        
        def dfs(i):
            if i in visited: # Cycle detection with backtracking
                return False
            if edges[i] == []: # if no prereqs, this edge is already good
                return True
            
            visited.add(i)
            # add children
            for c in edges[i]:
                if not dfs(c):
                    return False
                edges[c] = [] # Might as well not have prereqs if there is a path to goal for c
            visited.remove(i)
            return True
            
        
        # Note that cycles are not allowed
        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
            
            
        return True

                

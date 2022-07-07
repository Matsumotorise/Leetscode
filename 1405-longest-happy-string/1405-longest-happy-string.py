class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        heap = [x for x in ((-a, 'a'),(-b, 'b'),(-c, 'c')) if x[0] != 0] # minheap
        cooling = None
        heapq.heapify(heap)
        
        res = []
        
        i = 0
        while heap:
            cnt, char = heapq.heappop(heap)
            if cooling:
                heapq.heappush(heap, cooling)
                cooling = None
            
            # failure conditions?
            if len(res) >= 2 and res[-1] == res[-2] == char:
                cooling = (cnt, char)
                continue
            
            res.append(char)
            if cnt+1 != 0:
                heapq.heappush(heap,(cnt+1, char))
            
        return "".join(res)
        
        
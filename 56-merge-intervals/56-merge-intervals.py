class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        
        lst = [intervals[0]]
        
        
        for inter in intervals[1:]:
            
            if lst[-1][1] >= inter[0]: # are intersecting
                lst[-1][1] = max(inter[1], lst[-1][1])
            else:
                lst.append(inter)
                
        return lst
            
        
        
        
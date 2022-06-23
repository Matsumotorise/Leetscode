class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        
        
        lastInterval = intervals[0]
        count = 0
        
        
        for inter in intervals[1:]:
            # include or exclude?
            
            # over lapping = exclude
            if lastInterval[1] > inter[0]: # interlapping
                count += 1
                lastInterval = inter if inter[1] <= lastInterval[1] else lastInterval # heuristic-ly get leftmost interval (greedy)
            elif lastInterval[1] <= inter[1]:
                lastInterval = inter
                
                
        return count
        
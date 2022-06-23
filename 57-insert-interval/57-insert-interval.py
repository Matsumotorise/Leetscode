class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        
        
        for idx, i in enumerate(intervals):
            # if the right interval is not yet intersecting
            if i[1] < newInterval[0]:
                ret.append(i)
            # if left interval has left the intersecting zone
            elif i[0] > newInterval[1]:
                ret.append(newInterval)
                ret.extend(intervals[idx:])
                return ret
            else: # we are intersecting somehow
                newInterval = [min(newInterval[0],i[0]), max(newInterval[1], i[1])]
                
        ret.append(newInterval)
        
        return ret
                
                
        
        
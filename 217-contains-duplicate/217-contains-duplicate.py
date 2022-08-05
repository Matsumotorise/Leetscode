class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        return any(map(lambda x: x>=2, Counter(nums).values()))
        
        #TLE
        #from itertools import combinations
        #return any(x[0] == x[1] for x in combinations(nums, 2))
        
        
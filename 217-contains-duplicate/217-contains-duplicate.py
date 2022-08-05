class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) space, O(n) time
        #from collections import Counter
        #return any(map(lambda x: x>=2, Counter(nums).values()))
    
        ''' #TLE O(n^2) time, O(1) space
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j and n1 == n2:
                        return True
        return False
        '''
        
        nums.sort()
        for n1, n2 in zip(nums[1:], nums):
            if n1 == n2:
                return True
        
    
        #TLE
        #from itertools import combinations
        #return any(x[0] == x[1] for x in combinations(nums, 2))
        
        
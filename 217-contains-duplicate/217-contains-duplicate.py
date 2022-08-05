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
        
        ''' TLE O(nlogn) time, O(1) space, inplace
        nums.sort()
        for n1, n2 in zip(nums[1:], nums):
            if n1 == n2:
                return True
        '''
        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            i+=1
            j+=1
        return False
        
       
    
        #TLE
        #from itertools import combinations
        #return any(x[0] == x[1] for x in combinations(nums, 2))
        
        
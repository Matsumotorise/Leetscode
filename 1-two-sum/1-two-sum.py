class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # num = a + b, num - a = b <-  find b
        hm = {}
        
        for i, n in enumerate(nums):
            if n in hm:
                return [hm[n], i]
            hm[target-n] = i
        
        return [-1,-1]
        '''
        for i, n in enumerate(nums):  # O(n)
            # Create O(1) lookups for num - a 
            hm[target - n] = i
        
        # O(n)
        for i, b in enumerate(nums):
            if b in hm and i != hm[b]:
                return [i, hm[b]]
        '''
                
        
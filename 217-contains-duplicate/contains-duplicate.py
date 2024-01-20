import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = collections.Counter(nums)
        return any(x[1]>1 for x in hm.items())




        
        
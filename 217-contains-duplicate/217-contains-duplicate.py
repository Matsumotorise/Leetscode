class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        return any(map(lambda x: x>=2, Counter(nums).values()))
        
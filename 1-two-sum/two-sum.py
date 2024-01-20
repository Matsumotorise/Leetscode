import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea: get a list of nums - target
        # If any other number in target - nums1-nums2 = 0, we have our two indicies
        modList = {target-n:i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            if n in modList and modList[n] != i:
                return modList[n], i
        return [-1,-1]

        




        
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = collections.Counter(nums)
        sortedItems = [x[0] for x in sorted(cntr.items(), key=lambda x: x[1])]
        return sortedItems[-k:]


        
        
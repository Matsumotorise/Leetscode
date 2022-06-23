class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        ret = nums[0]
        
        # voting algo
        for i in range(1, len(nums)):
            # if they agree, raise counter by 1, otherwise - 1
            if nums[i] == ret:
                count += 1
            else:
                count -= 1
            
            # Now, if they equal out, 
            if count == 0:
                count = 1
                ret = nums[i]
        
        return ret
        
        
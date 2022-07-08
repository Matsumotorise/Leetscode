class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        
        
        while l <= r:
            mid = l + ((r-l) // 2)
            
            decRight = mid+1 >= len(nums) or nums[mid] > nums[mid+1]
            decLeft = mid - 1 < 0 or nums[mid-1] < nums[mid]
            
            
            if decRight and decLeft: # perfect
                return mid
            elif decRight: # shrink right
                r = mid - 1
            else: # shrink left
                l = mid + 1
            
            
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers)-1
        
        while r > l:
            curSum = numbers[r]+numbers[l]
            # two cases
            # Case 1:
            if curSum < target:
                l+=1
            # Case 2:
            elif curSum > target:
                r-=1
            # Case 3:
            else:
                return [l+1,r+1]
        
        return None
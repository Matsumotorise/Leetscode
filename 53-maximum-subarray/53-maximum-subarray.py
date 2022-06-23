class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Heuristic if 0 reset to 0
        runningSum = 0
        maxRes = nums[0]
        
        for n in nums:
            runningSum += n
            maxRes = max(runningSum, maxRes)
            if runningSum < 0: # Cut your losses for next itteration
                runningSum = 0
        return maxRes
                
            
        
        '''
        # divide and conquer
        def helper(arr, code):
            if(len(arr) == 1):
                return arr[0] , 0b11
            a = arr[:len(arr)//2]
            b = arr[len(arr)//2:]
            
            # recursive step
            if(code & (1 << 0)):
                resA = helper(a)
            else:
                resA = -float('inf')
            if (code & (1<<1)):
                resB = helper(b)
            else:
                resB = -float('inf')
            
            # merge step
            
        
        return helper(nums)[0]
        '''
            
            
            
        
        
            

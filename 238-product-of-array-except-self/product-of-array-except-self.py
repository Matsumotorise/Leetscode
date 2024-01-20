class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftAsc = [1]*len(nums)
        rightAsc = [1]*len(nums)
        product = [1]*len(nums)

        for i in range(len(nums)-1):
            leftAsc[i+1] = leftAsc[i] * nums[i]
            rightAsc[len(nums) - 2 - i] *= rightAsc[len(nums)-i-1] * nums[len(nums)-1-i]
        
        for i in range(len(product)):
            product[i] = leftAsc[i]*rightAsc[i]
        return product

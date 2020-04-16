class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        right_mult = nums[-1]
        for i in reversed(range(0, len(nums) - 1)):
            output[i] = output[i] * right_mult
            right_mult *= nums[i]

        return output
        

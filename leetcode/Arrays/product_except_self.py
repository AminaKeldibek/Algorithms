class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in xrange(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in xrange(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [x * y for x, y in zip(left, right)]


class SolutionConstSpace(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = [1] * len(nums)
        temp_right = 1

        for i in xrange(1, len(nums)):
            prod[i] = prod[i - 1] * nums[i - 1]
        for i in xrange(len(nums) - 2, -1, -1):
            temp_right *= nums[i + 1]
            prod[i] = prod[i] * temp_right

        return prod

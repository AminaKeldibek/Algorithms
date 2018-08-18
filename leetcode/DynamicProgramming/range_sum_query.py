class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        self.nums = nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i != 0:
            return self.nums[j] - self.nums[i - 1]
        else:
            return self.nums[j]

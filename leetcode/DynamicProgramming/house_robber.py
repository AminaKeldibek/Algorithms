class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_sum_by_idx = [0] * len(nums)
        max_sum_by_idx[0] = nums[0]
        max_sum_by_idx[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            new_sum = nums[i] + max_sum_by_idx[i - 2]
            max_sum_by_idx[i] = max(max_sum_by_idx[i - 1], new_sum)

        return max_sum_by_idx[len(nums) - 1]

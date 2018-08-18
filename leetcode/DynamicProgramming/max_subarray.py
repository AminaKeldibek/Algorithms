class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxSubArrayDivConq(nums):
            def maxSubArrayWithStart(nums, mid_idx):
                max_sum_left = nums[mid_idx - 1]
                max_sum_right = nums[mid_idx]

                for i in range(mid_idx - 2, -1, -1):
                    cur_sum = sum(nums[i:mid_idx])
                    if cur_sum > max_sum_left:
                        max_sum_left = cur_sum

                for i in range(mid_idx + 2, len(nums) + 1):
                    cur_sum = sum(nums[mid_idx:i])
                    if cur_sum > max_sum_right:
                        max_sum_right = cur_sum

                return max_sum_left + max_sum_right

            if len(nums) == 1:
                return nums[0]

            mid_idx = int(len(nums) / 2)
            sum_left = maxSubArrayDivConq(nums[0:mid_idx])
            sum_right = maxSubArrayDivConq(nums[mid_idx:len(nums)])
            sum_center = maxSubArrayWithStart(nums, mid_idx)

            return max(sum_left, sum_right, sum_center)

        return maxSubArrayDivConq(nums)

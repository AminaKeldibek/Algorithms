class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in nums:
                cur_len = 1
                cur_num = num

                while cur_num + 1 in nums:
                    cur_len += 1
                    cur_num += 1
                max_len = max(max_len, cur_len)

        return max_len

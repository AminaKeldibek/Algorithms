class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max_len = [1] * len(nums)
        seq_count = [1] * len(nums)

        max_len = 1
        res = 0

        for i in xrange(1, len(nums)):
            for j in xrange(0, i):
                if nums[j] < nums[i]:
                    if cur_max_len[j] + 1 > cur_max_len[i]:
                        seq_count[i] = seq_count[j]
                        cur_max_len[i] = cur_max_len[j] + 1
                    elif cur_max_len[j] + 1 == cur_max_len[i]:
                        seq_count[i] += seq_count[j]
            max_len = max(max_len, cur_max_len[i])

        for i in xrange(0, len(seq_count)):
            if cur_max_len[i] == max_len:
                res += seq_count[i]
        return res
        

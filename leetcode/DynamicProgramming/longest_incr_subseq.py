class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def BinSearch (idx, T, nums):
            l = 0
            r = len(T) - 1
            while (r - l) >= 1:
                m = l + (r - l) / 2
                if nums[idx] > nums[T[m]]:
                    l = m + 1
                else:
                    r = m
            if nums[idx] > nums[T[r]]:
                return -1
            return r

        if not nums:
            return 0

        max_len = 0
        T = [0]

        for i in xrange(1, len(nums)):
            res = BinSearch(i, T, nums)
            if res == -1:
                max_len += 1
                T.append(i)
            else:
                T[res] = i

        return max_len + 1

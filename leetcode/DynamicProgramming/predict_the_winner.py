class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True


        dp = [None] * len(nums)
        for i in xrange(0, len(nums)):
            dp[i] = [None] * len(nums)

        for i in xrange(0, len(nums)):
            dp[i][i] = nums[i]

        print dp
        def GetScore(i, j):
            if dp[i][j] is None:
                dp[i][j] = max(nums[i] - GetScore(i + 1, j), nums[j] - GetScore(i, j - 1))
            return dp[i][j]
        return GetScore(0, len(nums) - 1) >= 0

        

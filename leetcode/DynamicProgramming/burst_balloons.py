class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        if l == 0:
            return 1
        if l == 1:
            return nums[0]

        S = [None] * l
        for i in range(0, l):
            S[i] = [0] * l

        for i in range(1, l - 1):
            S[i][i] = nums[i] * nums[i - 1] * nums[i + 1]
        S[0][0] = nums[0] * nums[1]
        S[l - 1][l - 1] = nums[l - 1] * nums[l - 2]

        for sub_l in range(2, l + 1):
            for i in range(0, l - sub_l + 1):
                j = i + sub_l
                left_balloon = 1
                right_baloon = 1

                if i > 0:
                    left_balloon = nums[i - 1]
                if j < l:
                    right_baloon = nums[j]
                for k in range(i, j):
                    score_left = 0
                    score_right = 0
                    if k > i:
                        score_left = S[i][k - 1]
                    if k < (j - 1):
                        score_right = S[k + 1][j - 1]
                    cur_score = score_left + score_right
                    cur_score += nums[k] * left_balloon * right_baloon
                    S[i][j - 1] = max(S[i][j - 1], cur_score)

        return S[0][l - 1]

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(n):
            if n not in memo:
                memo[n] = n
                for div in range(2, n / 2):
                    quot, rem = divmod(n, div)
                    if rem == 0:
                        memo[n] = div + dp(quot)
                        break

            return memo[n]

        memo = {1: 0, 2: 2, 3: 3}

        return dp(n)

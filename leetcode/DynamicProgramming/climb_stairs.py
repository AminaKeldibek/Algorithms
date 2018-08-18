class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = [0] * (n + 1)
        M[0] = 1
        M[1] = 1

        for i in range(2, n + 1):
            M[i] = M[i - 1] + M[i - 2]

        return M[n]
        

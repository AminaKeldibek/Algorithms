class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def findIntBreak(n):
            precalc_seq = [0, 1, 1, 2, 4, 6, 9]
            if n <= 6:
                return precalc_seq[n]
            return 3 * findIntBreak(n - 3)

        return findIntBreak(n)

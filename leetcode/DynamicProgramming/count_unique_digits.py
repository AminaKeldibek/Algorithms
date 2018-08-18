class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        counts = [0] * n
        counts[0] = 10
        counts[1] = 81

        res = 91
        for i in range(2, n):
            counts[i] = counts[i - 1] * (10 - i)
            res += counts[i]

        return res

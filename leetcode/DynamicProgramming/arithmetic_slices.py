class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ap_prev = 0
        sum = 0

        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                sum += (1 + ap_prev)
                ap_prev = 1 + ap_prev
            else:
                ap_prev = 0

        return sum

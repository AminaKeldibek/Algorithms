class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        idx_even = 0
        idx_odd = 1
        A_sorted = [None] * len(A)

        for num in A:
            if num % 2 == 0:
                A_sorted[idx_even] = num
                idx_even += 2
            else:
                A_sorted[idx_odd] = num
                idx_odd += 2

        return A_sorted

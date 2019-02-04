class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        pos_idx, neg_idx = len(A) - 1, -1
        for i in range(len(A)):
            if A[i] >= 0:
                pos_idx = i
                neg_idx = i - 1
                break

        while pos_idx < len(A) and neg_idx >= 0:
            l, r = pow(A[neg_idx], 2), pow(A[pos_idx], 2)
            if l <= r:
                res.append(l)
                neg_idx -= 1
            else:
                res.append(r)
                pos_idx += 1
        while neg_idx >= 0:
            res.append(pow(A[neg_idx], 2))
            neg_idx -= 1
        while pos_idx < len(A):
            res.append(pow(A[pos_idx], 2))
            pos_idx += 1

        return res

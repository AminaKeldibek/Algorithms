class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def flip_row(row):
            med = len(row) / 2
            last_idx = len(row) - 1
            for i in range(med):
                temp = row[i]
                row[i] = row[last_idx - i]
                row[last_idx - i] = temp
            return row

        def invert_num(x):
            if x == 0:
                return 1
            else:
                return 0

        for i in range(len(A)):
            A[i] = flip_row(A[i])

        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = invert_num(A[i][j])

        return A

        

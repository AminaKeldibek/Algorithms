class Solution(object):
    def sortArrayByParityMergeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return (A)
        mid = len(A) / 2
        left,right = self.sortArrayByParity(A[:mid]), self.sortArrayByParity(A[mid:])
        out = []

        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right) and (left[left_idx] % 2 == 0 or right[right_idx] % 2 == 0):
            if left[left_idx] % 2 == 0:
                out.append(left[left_idx])
                left_idx += 1
            if right[right_idx] % 2 == 0:
                out.append(right[right_idx])
                right_idx += 1

        while left_idx < len(left):
                out.append(left[left_idx])
                left_idx += 1

        while right_idx < len(right):
                out.append(right[right_idx])
                right_idx += 1

        return out

    def sortArrayByParityLists(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return (A)
        even = []
        odd = []
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        return even + odd

    def sortArrayByParityInPlace(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return (A)
        swap_idx = len(A) - 1
        i = 0
        while i != swap_idx:
            if A[i] % 2 > 0:
                temp = A[i]
                A[i] = A[swap_idx]
                A[swap_idx] = temp
                swap_idx -= 1
            else:
                i += 1

        return A

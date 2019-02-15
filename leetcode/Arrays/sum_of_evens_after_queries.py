class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        out = []
        cur_sum = sum([n for n in A if n % 2 == 0])

        for val, idx in queries:
            prev_val = A[idx]
            A[idx] += val
            prev_is_even = prev_val % 2 == 0
            cur_is_even = A[idx] % 2 == 0

            if not prev_is_even and cur_is_even:
                cur_sum += A[idx]
            elif prev_is_even:
                if cur_is_even:
                    cur_sum += val
                else:
                    cur_sum -= prev_val
            out.append(cur_sum)

        return (out)
        

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def ComplSign(x):
            if x > 0: return -1
            return 1

        if k == 1:
            return range(1, n + 1)

        cur_num = 1
        out = [1]
        step = n - 1
        while k > 1:
            cur_num += step
            out.append(cur_num)
            step = ComplSign(step) * (abs(step) - 1)
            print step
            k -= 1
        if out[-2] > out[-1]:
            seq = range(out[-1] + 1, out[-2])
        else:
            seq = range(out[-1] - 1, out[-2], -1)

        out += seq

        return out

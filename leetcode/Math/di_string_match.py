class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)
        res = []
        for s in S:
            if s == "I":
                res.append(lo)
                lo += 1
            if s == "D":
                res.append(hi)
                hi -= 1
        res += [lo]

        return res

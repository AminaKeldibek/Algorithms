from math import log

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        idxs = [i for i in xrange(0, int(log(N, 2) + 1)) if N>>i & 1]
        if len(idxs) < 2:
            return 0
        return max([idxs[i] - idxs[i - 1] for i in xrange(1, len(idxs))])

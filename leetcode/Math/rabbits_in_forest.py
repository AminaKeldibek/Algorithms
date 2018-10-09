from collections import defaultdict
import math

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        res = 0
        for i in answers:
            d[i] += 1
        for k, v in d.iteritems():
            if v <= k + 1:
                res += (k + 1)
            else:
                res += math.ceil(float(v) / (k + 1)) * (k + 1)
        return int(res)

                

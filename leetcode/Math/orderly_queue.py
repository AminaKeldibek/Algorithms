class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            min_substr = S
            for i in xrange(0, len(S)):
                if S[i:] + S[:i] < min_substr:
                    min_substr = S[i:] + S[:i]
            return min_substr
        else:
            return ''.join(sorted(S))
                

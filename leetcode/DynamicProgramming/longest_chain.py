class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda p: p[1])
        max_seq = 1
        y_cur = pairs[0][1]

        for i in range(1, len(pairs)):
            if pairs[i][0] > y_cur:
                y_cur = pairs[i][1]
                max_seq += 1

        return max_seq

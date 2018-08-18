class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        S = [None] * (len(word1) + 1)
        for i in range(0, len(S)):
            S[i] = [None] * (len(word2) + 1)

        for i in range(0, len(S) - 1):
            S[i][-1] = len(word1) - i

        for j in range(0, len(S[0]) - 1):
            S[-1][j] = len(word2) - j
        S[-1][-1] = 0

        for i in xrange(len(word1) - 1, -1, -1):
            for j in xrange(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    S[i][j] = S[i + 1][j + 1]
                else:
                    S[i][j] = 1 + min(S[i + 1][j], S[i + 1][j + 1], S[i][j + 1])

        return S[0][0]

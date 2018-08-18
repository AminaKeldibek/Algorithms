class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def GetStrVal(s):
            return sum([ord(n) for n in s])

        def FindMinCost(s1, s2, k1, k2, S):
            if k1 == len(s1):
                return GetStrVal(s2[k2:])
            if k2 == len(s2):
                return GetStrVal(s1[k1:])
            if s1[k1:] == s2[k2:]:
                return 0

            cost = 0
            if S[k1][k2] == -1:
                if s1[k1] == s2[k2]:
                    cost += FindMinCost(s1, s2, k1 + 1, k2 + 1, S)
                else:
                    cost += min(
                        ord(s2[k2]) + FindMinCost(s1, s2, k1, k2 + 1, S),
                        ord(s1[k1]) + FindMinCost(s1, s2, k1 + 1, k2, S)
                    )
                S[k1][k2] = cost

            return S[k1][k2]

        S = [None] * len(s1)
        for i in range(0, len(s1)):
            S[i] = [-1] * len(s2)

        return FindMinCost(s1, s2, 0, 0, S)

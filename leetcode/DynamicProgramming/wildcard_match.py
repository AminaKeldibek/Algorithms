import unittest


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def NormPattern(p):
            p2 = p[0]
            for i in range(1, len(p)):
                if p[i] == '*':
                    if p2[-1] != '*':
                        p2 += p[i]
                else:
                    p2 = p2 + p[i]
            return p2

        def InitMemoMat(s, p):
            S = [None] * (len(s) + 1)
            for i in range(0, len(s)):
                S[i] = [None] * len(p)
            S[-1] = [False] * len(p)

            if p[-1] == '*':
                for i in range(0, len(S)):
                    S[i][-1] = True
            else:
                for i in range(0, len(S)):
                    S[i][-1] = False
                S[-2][-1] = p[-1] == s[-1] or p[-1] == '?'

            return S

        def F(i, j):
            if S[i][j] is None:
                if p[j] == '*':
                    res = False
                    for n in range(i, len(s)):
                        res = res or F(n, j + 1)
                else:
                    res = s[i] == p[j] or p[j] == '?'
                    if res:
                        res = res and F(i + 1, j + 1)

                S[i][j] = res

            return S[i][j]

        if len(p) == 0:
            return len(s) == 0
        if p == '*':
            return True
        if len(s) == 0 and p not in ['*', '']:
            return False

        p = NormPattern(p)
        S = InitMemoMat(s, p)

        return F(0, 0)


class TestSolution(unittest.TestCase):
    def test_symbols(self):
        s = ['abc', 'xyz', 'xyz', '', 'xyz']
        p = ['abc', 'abc', 'xyc', '', '']
        out = [True, False, False, True, False]
        for i in range(0, len(s)):
            self.assertEqual(Solution().isMatch(s[i], p[i]), out[i])

    def test_star(self):
        s = ['abc', 'abc', '', 'abc']
        p = ['a*c', 'a*d', '*', '*']
        out = [True, False, True, True]
        for i in range(0, len(s)):
            self.assertEqual(Solution().isMatch(s[i], p[i]), out[i])

    def test_question(self):
        s = ['abc', 'abc', 'abc', '']
        p = ['a?c', '???', '?bz', '?']
        out = [True, True, False, False]
        for i in range(0, len(s)):
            self.assertEqual(Solution().isMatch(s[i], p[i]), out[i])

    def test_mixed(self):
        s = ["mississippi", "a", "ho"]
        p = ["m??*ss*?i*pi", "a*", "ho**"]
        out = [False, True, True]
        for i in range(0, len(s)):
            self.assertEqual(Solution().isMatch(s[i], p[i]), out[i])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    unittest.TextTestRunner(verbosity=2).run(suite)

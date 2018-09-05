class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 9 if s[0] == '*' else 0 if s[0] == '0' else 1
        buf_size = 3
        dp = [None] * buf_size
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 0 if s[0] == '0' else 1

        for i in range(1, len(s)):
            if s[i] != '*':
                if s[i] != '0':
                    dp[(i + 1) % buf_size] = dp[i % buf_size]
                else:
                    dp[(i + 1) % buf_size] = 0
                if s[i - 1] == '*':
                    if s[i] < '7':
                        dp[(i + 1) % buf_size] += 2 * dp[(i - 1) % buf_size]
                    else:
                        dp[(i + 1) % buf_size] += dp[(i - 1) % buf_size]
                else:
                    if s[i - 1:i + 1] < '27' and s[i - 1] != '0':
                        dp[(i + 1) % buf_size] += dp[(i - 1) % buf_size]
            else:
                dp[(i + 1) % buf_size] = 9 * dp[i % buf_size]
                if s[i - 1] == '*':
                    dp[(i + 1) % buf_size] += 15 * dp[(i - 1) % buf_size]
                elif s[i - 1] == '1':
                    dp[(i + 1) % buf_size] += 9 * dp[(i - 1) % buf_size]
                elif s[i - 1] == '2':
                    dp[(i + 1) % buf_size] += 6 * dp[(i - 1) % buf_size]

        return dp[(i + 1) % buf_size] % (pow(10, 9) + 7)

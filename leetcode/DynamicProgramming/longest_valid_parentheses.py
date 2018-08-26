def longestValidParenthesesBruteForce(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2:
        return 0

    res = 0
    for l in xrange(2, len(s) + 1, 2):
        for i in range(0, len(s) - l + 1):
            sum = 0
            for j in range(i, i + l):
                if s[j] == '(' and sum >= 0:
                    sum += 1
                elif s[j] == ')':
                    sum -= 1
            if sum == 0:
                res = max(res, l)

    return res


def longestValidParenthesesDP(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2:
        return 0

    dp = [0] * len(s)
    max_len = 0

    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ')':
                if dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(' and (i - dp[i - 1]) > 0:
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
            max_len = max(max_len, dp[i])

    return max_len


def longestValidParenthesesStack(self, s):
    """
    :type s: str
    :rtype: int
    """
    stack = [-1]
    max_len = 0

    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


def longestValidParenthesesConstSpace(self, s):
    """
    :type s: str
    :rtype: int
    """
    left, right = 0, 0
    max_len = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1
        if left == right:
            max_len = max(max_len, left + right)
        if right > left:
            left, right = 0, 0

    left, right = 0, 0
    for i in xrange(len(s) - 1, -1, -1):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1
        if left == right:
            max_len = max(max_len, left + right)
        if left > right:
            left, right = 0, 0

    return max_len

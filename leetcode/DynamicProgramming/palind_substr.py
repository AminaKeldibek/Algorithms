class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 1):
            return 1

        if len(s) == 2:
            if s[0] == s[1]:
                return 3
            else:
                return 2

        count = len(s)
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                k = 1
                while (i - k) > -1 and (i + 1 + k) < len(s):
                    if s[i - k] != s[i + 1 + k]:
                        break
                    count += 1
                    k += 1

        for i in range(1, len(s) - 1):
            k = 1
            while (i - k) > -1 and (i + k) < len(s):
                if s[i - k] != s[i + k]:
                    break
                count += 1
                k += 1

        return count

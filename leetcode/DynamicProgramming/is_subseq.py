class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_idx, t_idx = 0, 0
        while t_idx < len(t) and s_idx < len(s):
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)
        

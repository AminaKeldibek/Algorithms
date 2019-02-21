class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new_str = ""
        for s in str:
            if s >= 'A' and s <= 'Z':
                new_str += chr(ord(s) + 32)
            else:
                new_str += s

        return new_str

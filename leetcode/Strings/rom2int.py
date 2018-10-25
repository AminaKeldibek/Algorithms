class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_2_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                         'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                         'XC': 90, 'CD': 400, 'CM': 900}
        res = 0
        i = 0
        while i < len(s) - 1:
            if (s[i] == 'I' and s[i + 1] in ['V', 'X']) or (s[i] == 'X' and
            s[i + 1] in ['L', 'C']) or (s[i] == 'C' and s[i + 1] in ['D', 'M']):
                    res += rom_2_int_map[s[i:i + 2]]
                    i = i + 2
            else:
                res += rom_2_int_map[s[i]]
                i = i + 1
        if i < len(s):
            res += rom_2_int_map[s[i]]

        return res

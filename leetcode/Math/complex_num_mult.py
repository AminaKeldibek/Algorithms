class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def parseStr(s):
            s = s.split("+")
            s[1] = s[1].replace("i", "")
            s = [int(el) for el in s]
            return s

        a, b = map(parseStr, (a, b))
        res_real = a[0]*b[0] - a[1] * b[1]
        res_imag = a[1]*b[0] + a[0]*b[1]

        return str(res_real) + "+" + str(res_imag) + "i"

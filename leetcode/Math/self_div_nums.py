class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # 68 ms
        '''def self_dividing(target):
            if target % 10 == 0:
                return False
            if target in range(1, 10):
                return True
            nums = str(target)
            for n in nums:
                int_n = int(n)
                if int_n == 0 or target % int_n != 0:
                    return False
            return True'''

        # 36 ms
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True


        out = []
        for target in range(left, right + 1):
            if self_dividing(target):
                out.append(target)

        return out

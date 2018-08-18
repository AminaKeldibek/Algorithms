class Solution(object):
     def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]

        bit_one_count = [1] * (num + 1)
        bit_one_count[0] = 0
        num_bits = 1

        for i in range(2, num + 1):
            if i >= pow(2, num_bits):
                num_bits += 1
            bit_one_count[i] += bit_one_count[i % pow(2, num_bits - 1)]

        return bit_one_count

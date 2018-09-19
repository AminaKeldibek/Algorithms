class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res, max_num = 0, 0

        for i, num in enumerate(arr):
            max_num = max(max_num, num)
            if max_num == i:
                res += 1
        return res
        

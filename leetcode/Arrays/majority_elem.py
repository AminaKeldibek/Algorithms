class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            if value == candidate:
                count += 1
            else:
                count -= 1

        return candidate

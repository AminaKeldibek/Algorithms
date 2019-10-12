class Solution(object):
    def checkSubarray(self, nums, start_idx, end_idx):
        if len(set(nums[start_idx:end_idx + 1])) == 1:
            return 0

        min_val = 10e1000
        max_val = -10e1000
        min_idx = None
        max_idx = None

        for i in range(start_idx, end_idx + 1):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i

        for j in range(end_idx, start_idx - 1, -1):
            if nums[j] > max_val:
                max_val = nums[j]
                max_idx = j

        if min_idx != start_idx and max_idx != end_idx:
            return (end_idx - start_idx + 1)

        if min_idx == start_idx:
            start_idx += 1
        if max_idx == end_idx:
            end_idx -= 1

        return self.checkSubarray(nums, start_idx, end_idx)

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.checkSubarray(nums, 0, len(nums) - 1)


class SolutionSelectionSort(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_idx = len(nums) - 1
        end_idx = 0

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    start_idx = min(start_idx, i)
                    end_idx = max(end_idx, j)

        if end_idx == 0:
            return 0
        return end_idx - start_idx + 1


class SolutionSorted(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_idx = len(nums) - 1
        end_idx = 0
        nums_sorted = sorted(nums)

        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                start_idx = min(start_idx, i)
                end_idx = max(end_idx, i)
        if end_idx == 0:
            return 0

        return end_idx - start_idx + 1

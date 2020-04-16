class LongSolution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_len = 0
        M = [None] * len(nums)
        for i in range(len(nums)):
            M[i] = [None] * len(nums)

        for i in range(0, len(nums) - 1):
            M[i][i+1] = len([x for x in nums[i:i+2] if x == 0])
            if M[i][i+1] == 1:
                max_len = 2

        if len(nums) > 2:
            for seq_len in range(3, len(nums) + 1):
                for i in range(len(nums) - seq_len + 1):
                    last_idx = i + seq_len - 1
                    if seq_len % 2 == 0:
                        M[i][last_idx] = M[i][last_idx - 1] + int(nums[last_idx] == 0)
                        if M[i][last_idx] == seq_len / 2:
                            max_len = seq_len
                    else:
                        M[i][last_idx] = M[i][last_idx - 1] + int(nums[last_idx] == 0)


        return max_len


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        count = 0
        count_dict = {0: 0}
        for idx, val in enumerate(nums, 1):
            if val == 1:
                count += 1
            else:
                count -= 1
            if count in count_dict:
                max_len = max(max_len, idx - count_dict[count])
            else:
                count_dict[count] = idx


        return max_len

"""
Submit here: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/
"""

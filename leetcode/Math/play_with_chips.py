class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        sum_evens = 0
        sum_odds = 0
        for i in chips:
            if i % 2 == 0:
                sum_evens += 1
            else:
                sum_odds += 1

        return min(sum_evens, sum_odds)
        

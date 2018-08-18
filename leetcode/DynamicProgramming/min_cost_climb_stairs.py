class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1:
            return cost[0]

        if len(cost) == 0:
            return 0

        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return min(cost[len(cost) - 1], cost[len(cost) - 2])
        

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = [None] * len(grid)
        for i in range(len(cost)):
            cost[i] = [None] * len(grid[0])

        cost[0][0] = grid[0][0]
        for i in range(1, len(cost[0])):
            cost[0][i] = cost[0][i - 1] + grid[0][i]

        for i in range(1, len(cost)):
            cost[i][0] = cost[i - 1][0] + grid[i][0]

        for i in range(1, len(cost)):
            for j in range(1, len(cost[0])):
                cost[i][j] = grid[i][j] + min(cost[i - 1][j], cost[i][j - 1])

        return cost[-1][-1]

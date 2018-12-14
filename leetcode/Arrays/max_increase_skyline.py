class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = [None] * len(grid)
        col_max = [0] * len(grid[0])
        total_sum = 0

        for i in xrange(0, len(grid)):
            row_max[i] = max(grid[i])
            for j in xrange(0, len(grid[0])):
                col_max[j] = max(col_max[j], grid[i][j])

        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[0])):
                total_sum += min(row_max[i], col_max[j]) - grid[i][j]

        return total_sum
            

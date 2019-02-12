class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = 0
        front = sum([max(row) for row in grid])

        col_max = [1] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    top += 1
                if grid[i][j] > col_max[j]:
                    col_max[j] = grid[i][j]
        side = sum(col_max)

        return top + front + side

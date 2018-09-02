class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
            """
            :type heights: List[int]
            :rtype: int
            """
            if len(heights) == 0:
                return 0
            if len(heights) == 1:
                return heights[0]

            area = 0
            max_area = -1
            stack = []
            i = 0
            while i < len(heights):
                if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                    i += 1
                else:
                    top = stack.pop()
                    if len(stack) == 0:
                        area = heights[top] * i
                    else:
                        area = heights[top] * (i - stack[-1] - 1)
                    max_area = max(max_area, area)

            while len(stack) != 0:
                top = stack.pop()
                if len(stack) == 0:
                    area = heights[top] * i
                else:
                    area = heights[top] * (i - stack[-1] - 1)
                max_area = max(max_area, area)

            return max_area

        max_area = 0
        if len(matrix) == 0:
            return 0

        cur_row = [0] * len(matrix[0])
        for i in range(0, len(matrix)):
            cur_row = [x1 + x2 for x1, x2 in zip(cur_row, map(int, matrix[i]))]
            for j in range(0, len(cur_row)):
                if matrix[i][j] == '0':
                    cur_row[j] = 0
            max_area = max(
                max_area,
                largestRectangleArea(cur_row)
            )

        return max_area

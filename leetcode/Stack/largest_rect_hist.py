class Solution(object):
    def largestRectangleArea(self, heights):
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

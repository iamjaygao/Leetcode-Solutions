class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (indx, height)

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                idx_stack, hi_stack = stack.pop()
                max_area = max(max_area,  hi_stack * (idx - idx_stack))
                start = idx_stack
            stack.append((start, height))
        
        for idx, hi in stack:
            max_area = max(max_area, hi * (len(heights) - idx))
        
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            pos = i
            while stack and stack[-1][1]>h:
                area = stack[-1][1]*(i-stack[-1][0])
                maxArea = max(maxArea, area)
                pos = stack[-1][0]
                stack.pop()
            stack.append((pos, h))
        
        n = len(heights)
        while stack:
            area = stack[-1][1]*(n-stack[-1][0])
            maxArea = max(maxArea, area)
            stack.pop()
        return maxArea
            
        
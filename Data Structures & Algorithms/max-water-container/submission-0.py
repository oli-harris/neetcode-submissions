class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            maxArea = max(maxArea, height * width)

            # left side lower
            if heights[l] < heights[r]:
                l += 1
            # right side lower / both side same
            else:
                r -= 1

        return maxArea
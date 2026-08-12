class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        current_max = min(heights[p1], heights[p2]) * p2
        while p2 > p1:
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
            current = min(heights[p1], heights[p2]) * (p2 - p1)
            if current > current_max:
                current_max = current
        

        return current_max
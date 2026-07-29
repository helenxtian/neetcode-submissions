class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, (len(heights)-1)
        max_area = 0
        while l < r:
            l_size = heights[l]
            r_size = heights[r]
            area = (r-l) * min(l_size, r_size)
            if area > max_area:
                max_area = area
            
            if l_size > r_size:
                r -= 1
            else:
                l += 1
        return max_area
class Solution:
    def trap(self, height: List[int]) -> int:
        # level != 0, don't save anything
        # heights[l] ><= heights[r], 

        # if heights of l or r == 0, move l or r
        # else
        # if (l+1) not > l and (r-)

        ### above doesn't make sense
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]] 
        for i in range(1,len(height)):
            if height[i] > left_max[i-1]:
                left_max.append(height[i])
            else:
                left_max.append(left_max[i-1])
        
        right_max = [0] * len(height)
        right_max[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        print(left_max)
        print(right_max)

        sum = 0
        for i in range(len(height)):
            sum += min(left_max[i], right_max[i]) - height[i]
        print(sum)
        return sum
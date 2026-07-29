class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the maximum is the min + length of the array
        nums = sorted(nums)
        print(nums)
        if not nums:
            return 0
            
        consecutive = [1]
        j=0
        for i in range(len(nums)):
            if (nums[i]==nums[i-1] or nums[i]==(nums[i-1]+1)):
                if (nums[i]==(nums[i-1]+1)):
                    consecutive[j] += 1
            else:
                j += 1
                consecutive.append(1)
        return max(consecutive)
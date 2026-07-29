class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            i_val = nums[i]
            diff = target - i_val
            new_nums = nums[i+1:]
            if diff in new_nums:
                diff_i = new_nums.index(diff) + i + 1
                return [i, diff_i]
            
        return None
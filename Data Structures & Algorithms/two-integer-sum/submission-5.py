class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_diff = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in nums_diff:
                return [nums_diff[diff],i]
            nums_diff[val] = i
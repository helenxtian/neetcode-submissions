class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a hash {number: diff = target - number}
        # check if diff exists in nums
        # need a hash for location, so {number : location}
        val_loc = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in val_loc:
                return [val_loc[diff], i]
            val_loc[nums[i]] = i
        return False

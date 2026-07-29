class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i in nums:
            if not i in unique:
                unique.append(i)
            else:
                return True
        return False
         
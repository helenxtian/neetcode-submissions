class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(0,len(nums)):
            prod = 1
            for j in range(0,len(nums)):
                if i != j:
                    prod = prod * nums[j]
            arr.append(prod)
        return arr

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers = sorted(numbers)
        #for i in range(len(numbers)):
        #    diff = target - numbers[i]
        #    if diff in numbers[i+1:]:
        #        diff_i = numbers.index(diff)
        #        return [i+1, diff_i+1]
        #return False

        l = 0
        r = len(numbers)-1

        while l < r:
            sum = numbers[l]+numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            elif sum == target:
                return[l+1, r+1]
        return False
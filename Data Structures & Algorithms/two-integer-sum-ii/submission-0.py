class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted(numbers)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers[i+1:]:
                diff_i = numbers.index(diff)
                return [i+1, diff_i+1]
        return False

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        sorted_nums = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
        return sorted_nums[:k]
        
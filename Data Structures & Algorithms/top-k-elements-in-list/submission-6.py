class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for n in nums:
            if n in elements.keys():
                elements[n] += 1
            else:
                elements[n] = 1
        sorted_desc = dict(sorted(elements.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_desc.keys())[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_freq = {}
        for i in nums:
            n_freq[i] = n_freq.get(i,0) + 1
        sorted_items = sorted(n_freq.items(), key=lambda item: item[1], reverse=True)
        return [n for n, freq in sorted_items[:k]]
        
        
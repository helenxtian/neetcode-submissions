class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i in anagrams:
                anagrams[sorted_i].append(i)
            else:
                anagrams[sorted_i] = [i]
        return list(anagrams.values())
        
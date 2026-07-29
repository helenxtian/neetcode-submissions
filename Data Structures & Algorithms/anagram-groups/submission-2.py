class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 
        for word in strs: 
            sorted_w = str(sorted(word))
            if sorted_w not in anagrams: 
                anagrams[sorted_w] = []
            anagrams[sorted_w].append(word)
        return list(anagrams.values())
        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # {sorted: [word1, word2, ...]}
       # time: O(N * K log K)
        """anagrams = {}
        for word in strs:
            sorted_w = str(sorted(word))
            if sorted_w not in anagrams:
                anagrams[sorted_w] = []
            anagrams[sorted_w].append(word)
        return list(anagrams.values())
        """

        # want time: O(N * K)
        anagrams = {}
        for word in strs:
            # rather than sorting, count freq of characters
            # use ascii, size 26
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in anagrams:
                anagrams[tuple(count)] = []
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())

        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # {letters : freq}
        if len(s) != len(t):
            return False

        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i],0) + 1
            counts[t[i]] = counts.get(t[i],0) - 1
        
        # if an anagram, all values should be 0
        for freq in counts.values():
            if freq != 0:
                return False
        return True

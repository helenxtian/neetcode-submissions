class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for i in s:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        
        for j in t:
            if j in char_count and char_count[j] > 0:
                char_count[j] -= 1
            else:
                return False
        return True
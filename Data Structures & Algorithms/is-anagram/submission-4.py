class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # {letter: freq}
        freak_s = {}
        freak_t = {}
        for letter in s:
            freak_s[letter] = freak_s.get(letter, 0) + 1
        for letter in t:
            freak_t[letter] = freak_t.get(letter, 0) + 1
        return (freak_s == freak_t)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            maxf = max(maxf, count[s[r]])
            while ((r+1)-l) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r+1)-l)
        return res
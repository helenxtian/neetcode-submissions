class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        # two pointers - left and right
        # keep expanding right pointer until all frequencies match
        # and then move left pointer right until not satisfied
        # if right pointer reaches end and the counts not satisfied, return ""
        countT = {}
        for i in range(len(t)):
            if t[i] in countT:
                countT[t[i]] += 1
            else:
                countT[t[i]] = 1

        l = 0
        countS = {}
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        for r in range(len(s)):
            letter = s[r]
            countS[letter] = 1 + countS.get(letter, 0)

            if letter in countT and countS[letter]==countT[letter]:
                have+=1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        
import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = {letter: 0 for letter in string.ascii_lowercase}
        s2_count = {letter: 0 for letter in string.ascii_lowercase}
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        matches = 0
        for i in string.ascii_lowercase:
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            i = s2[r]
            s2_count[i] += 1
            if s1_count[i] == s2_count[i]:
                matches += 1
            elif s1_count[i] + 1 == s2_count[i]:
                matches -= 1
            
            i_l = s2[l]
            s2_count[i_l] -= 1
            if s1_count[i_l] == s2_count[i_l]:
                matches += 1
            elif s1_count[i_l] - 1 == s2_count[i_l]:
                matches -= 1
            l +=1

        return matches == 26

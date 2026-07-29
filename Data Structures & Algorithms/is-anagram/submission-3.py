class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for s_letter in s:
            if s_letter not in s_dict:
                s_dict[s_letter] = 1
            else:
                s_dict[s_letter] += 1
        
        t_dict = {}
        for t_letter in t:
            if t_letter not in t_dict:
                t_dict[t_letter] = 1
            else:
                t_dict[t_letter] += 1
        
        if s_dict != t_dict:
            return False
        return True

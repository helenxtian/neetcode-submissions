class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        for i in strs:
            sorted_i = ''.join(sorted(i, key=str.lower))
            if sorted_i in final.keys():
                final[sorted_i].append(i)
            else:
                final[sorted_i] = [i]
        return list(final.values())

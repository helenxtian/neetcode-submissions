class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += f'{len(s)}#{s}'
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            arr.append(s[j+1:j+1+num])
            i = j + 1 + num
        return arr

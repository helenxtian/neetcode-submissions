class Solution:
    def encode(self, strs: List[str]) -> str:
        # start with number of elements
        # after each thing, put the length of it
        # str = ''.join(len(strs)) -- maybe unnecessary
        st = ''
        for i in strs:
            st += (f'{str(len(i))}#{i}')
        return st

    def decode(self, s: str) -> List[str]:
        out = []
        while s:
            i_hashtag = s.find('#')
            length = int(s[0:i_hashtag])
            out.append(s[(i_hashtag+1):(length+i_hashtag+1)])
            s = s[length+i_hashtag+1:]
        return out

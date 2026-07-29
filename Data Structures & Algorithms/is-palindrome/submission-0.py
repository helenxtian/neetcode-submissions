class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        l = len(s)
        for i in range(l//2):
            if s[i] != s[l-i-1]:
                return False
        return True
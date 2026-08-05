class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dp: T if idx j is reachable from idx 0/i (i has to be reachable from 0)
        # can jump from j if minJump <= i - j <= maxJump
        # minJump - i <= -j <= maxJump - i
        # i - minJump >= j >= i - maxJump
        # i - maxJump <= j <= i - minJump

        n = len(s)
        dp = [False] * n
        dp[0] = True

        for j in range(1, n):
            entering = j - maxJump
            leaving =  j - minJump

            if s[j] == '0':
                for i in range(entering, leaving+1):
                    if dp[i]:
                        dp[j] = True
        
        print(dp)
        return dp[n-1]

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        if n <= 0:
            return 0

        dp = [[False] * n for _ in range(n)]
        # [[False, False, False], [False, False, False], [False, False, False]]

        for i in range(n):
            dp[i][i] = True
            ans += 1
        # [[True, False, False], [False, True, False], [False, False, True]]

        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += 1 if dp[i][i + 1] else 0
        # [[True, True, False], [False, True, True], [False, False, True]]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                ans += 1 if dp[i][j] else 0
        # [[True, True, True], [False, True, True], [False, False, True]]

        return ans
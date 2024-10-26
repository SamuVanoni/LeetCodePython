class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ans = [0] * len(s)
        count = float('inf')  # Facilitate comparison

        # Left -> Right
        for i in range(len(s)):
            if s[i] == c:
                count = 0
            else:
                count += 1
            ans[i] = count

        print(ans) # [inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]

        count = float('inf')  # Reset the counter

        # Right -> left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                count = 0
            else:
                count += 1
            ans[i] = min(ans[i], count)  # Lowest value

        return ans
class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 2
        while (ans - 1) < n:
            ans *= 2
        return ans - 1
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 3 = 2 / 4 = 4 / 5 = 6 / 6 = 9 / 7 = 12
        # 2 / 1 + 3 / 2 + 4 / 1 + 3 + 5 / 2 + 4 + 6
        return n * n // 4
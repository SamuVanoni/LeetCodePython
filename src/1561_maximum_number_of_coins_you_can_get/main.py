class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        ans = 0
        n = len(piles)

        for i in range(n // 3, n, 2):
            ans += piles[i]

        return ans
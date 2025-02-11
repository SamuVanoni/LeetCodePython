class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        l = len(grid[0])

        while l > 0:
            countMax = 0
            for g in grid:
                if countMax < max(g):
                    countMax = max(g)
                g.remove(max(g))
            ans += countMax
            l -= 1
            
        return ans
class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        ans = {}

        for i in range(0, len(rings), 2):
            color = rings[i]
            ring = rings[i + 1]

            if ring not in ans:
                ans[ring] = set()  # Avoid duplicates
            ans[ring].add(color)

        # Adds 1 for each color in the rings and returns if = 3
        return sum(1 for colors in ans.values() if len(colors) == 3)
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        aux = heights[:]
        aux.sort()
        ans = 0
        for i in range(len(heights)):
            if aux[i] != heights[i]:
                ans += 1
        return ans
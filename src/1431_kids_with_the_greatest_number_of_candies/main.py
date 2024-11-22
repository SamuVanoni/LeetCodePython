class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        countMax = max(candies)
        ans = []
        for c in candies:
            if c + extraCandies >= countMax:
                ans.append(True)
            else:
                ans.append(False)
        return ans
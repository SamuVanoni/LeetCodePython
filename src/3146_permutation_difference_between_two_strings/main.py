class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        varSum = 0
        for i, value in enumerate(s):
            for j, value2 in enumerate(t):
                if value == value2:
                    varSum += abs(i - j)
        return varSum
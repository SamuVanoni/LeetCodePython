class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxCount = 0
        for letter in s:
            if letter == "(":
                count += 1
            if letter == ")":
                count -= 1
            if count > maxCount:
                maxCount = count
        return maxCount
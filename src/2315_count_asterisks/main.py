class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        sentinel = True
        for c in s:
            if c == "|":
                sentinel = not sentinel
            if c == "*" and sentinel:
                count += 1
        return count
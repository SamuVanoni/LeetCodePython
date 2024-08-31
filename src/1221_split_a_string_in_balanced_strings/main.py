class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        c = 0
        for i in range(len(s)):
            if s[i] == "R":
                count += 1
            else:
                count -= 1
            if count == 0:
                c += 1
        return c
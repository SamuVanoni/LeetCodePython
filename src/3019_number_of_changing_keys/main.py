class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = lower(s)
        for i, letter in enumerate(s):
            if letter != s[i-1] and i != 0:
                count += 1
        return count
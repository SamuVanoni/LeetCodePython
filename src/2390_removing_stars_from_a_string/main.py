class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for l in s:
            if l == "*":
                ans = ans[:-1]
            else:
                ans += l
        return ans
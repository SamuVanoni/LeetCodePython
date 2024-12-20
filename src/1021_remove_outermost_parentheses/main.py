class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        count = 0
        for l in s:
            if l == "(":
                count += 1
                if count >= 2:
                    ans += l
            if l == ")":
                count -= 1
                if count >= 1:
                    ans += l
        return ans
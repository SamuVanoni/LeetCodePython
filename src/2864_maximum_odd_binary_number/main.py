class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = s.count("1")
        ans = ""
        for i in range (len(s) - 1):
            if count > 1:
                ans += "1"
                count -= 1
            else:
                ans += "0"
        ans += "1"
        return ans
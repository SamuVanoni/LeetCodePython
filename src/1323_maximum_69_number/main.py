class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = ""
        find = False
        for d in str(num):
            if d == "6" and not find:
                ans += "9"
                find = True
            else:
                ans += d
        return int(ans)
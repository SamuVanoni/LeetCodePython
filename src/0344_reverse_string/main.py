class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s) - 1
        count = 0
        while l > count:
            s[count], s[l] = s[l], s[count]
            count += 1
            l -= 1
        return s
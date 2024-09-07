class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        for letter in s:
            if letter == 'i':
                r = r[::-1]
            else:
                r += letter
        return r
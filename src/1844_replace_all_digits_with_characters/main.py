class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i, letter in enumerate(s):
            if letter in numbers:
                count = ord(s[i-1]) + int(letter)
                ans += chr(count)
            else:
                ans += letter
        return ans
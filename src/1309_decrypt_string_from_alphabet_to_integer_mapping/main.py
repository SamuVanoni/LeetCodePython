class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i, letter in enumerate(s):
            if letter == '#':
                ans = ans[:-2]
                number = int(str(s[i-2]) + str(s[i-1])) + ord('a') - 1
                ans += chr(number)
            else:
                number = int(s[i]) + ord('a') - 1
                ans += chr(number)
        return ans
class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: inta
        :rtype: str
        """
        ans = ""
        for i in range(0, len(s), k):
            count = 0
            countSum = 0
            while count < k and (i + count) < len(s):
                countSum += ord(s[i + count].lower()) - ord('a')
                count += 1
            ans += chr(ord('a') + (countSum % 26))
        return ans
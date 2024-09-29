class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans = ''
        count = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] == '0':
                count += 1
            else:
                break
        for i in range(len(num) - count):
            ans += num[i]
        return ans
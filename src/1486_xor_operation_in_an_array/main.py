class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        count = []
        for i in range(n):
            count.append(start + (2 * (i)))
        ans = count[0]
        for i in range(1, n):
            ans = ans ^ count[i]
        return ans
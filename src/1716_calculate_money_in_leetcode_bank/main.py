class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        start = 1
        end = 7

        while (n - 7) > 0:
            for i in range(start, end+1):
                ans += i
            start += 1
            end += 1
            n -= 7

        while n != 0:
            ans += start
            start += 1
            n -= 1

        return ans   
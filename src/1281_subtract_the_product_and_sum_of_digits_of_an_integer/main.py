class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        s = 0
        for i in str(n):
            m *= int(i)
            s += int(i)
        return m - s
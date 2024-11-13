class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        count1 = 0
        count2 = 0
        for i in range(1, n+1):
            if i % m == 0:
                count2 += i
            else:
                count1 += i
        return count1 - count2
        
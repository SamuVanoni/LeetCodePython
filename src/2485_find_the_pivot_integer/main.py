class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = -1
        for i in range(n):
            count1 = 0
            count2 = 0
            for j in range(i+1):
                count1 += j+1
            for j in range(n, i, -1):
                count2 += j
            if count1 == count2:
                ans = i+1
        return ans
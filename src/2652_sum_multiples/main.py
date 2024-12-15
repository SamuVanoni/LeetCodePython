class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        count = 1
        while count <= n:
            if count % 3 == 0 or count % 5 == 0 or count % 7 == 0:
                ans += count
            count += 1
        return ans
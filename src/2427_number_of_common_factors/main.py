class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = 0
        count = 1
        while count <= a and count <= b:
            if a % count == 0 and b % count == 0:
                ans += 1
            count += 1
        return ans
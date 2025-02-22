class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        baseK = ""

        while (n // k) > 0:
            baseK += str(n % k)
            n = n // k
        baseK += str(n)

        return sum(int(d) for d in baseK) # if d.isdigit()
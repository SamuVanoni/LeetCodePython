class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        l = n // 2

        for i in range(l):
            ans.append(i+1)
            ans.append(-1 * (i+1))
        
        if n % 2 == 1:
            ans.append(0)
        
        return ans
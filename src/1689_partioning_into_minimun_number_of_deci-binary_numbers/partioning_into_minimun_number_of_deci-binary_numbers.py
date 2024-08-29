class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(n))
        # varMax = 0
        # for i in range(len(n)):
        #     if n[i] > varMax:
        #         varMax = n[i]
        # return int(varMax)
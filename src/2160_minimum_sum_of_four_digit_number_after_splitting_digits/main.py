class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = sorted(str(num))
        n1 = ""
        n2 = ""
        for i in range(len(l)):
            if i % 2 == 0:
                n1 += l[i]
            else:
                n2 += l[i]
        return int(n1) + int(n2)
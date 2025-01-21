class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def reverse(n):
            return int(str(n)[::-1])
        
        aux = reverse(num)
        aux = reverse(aux)

        if aux == num:
            return True
        return False

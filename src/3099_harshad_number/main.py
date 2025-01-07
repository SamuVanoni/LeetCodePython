class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        soma = sum(int(d) for d in str(x))
        return soma if x % soma == 0 else -1
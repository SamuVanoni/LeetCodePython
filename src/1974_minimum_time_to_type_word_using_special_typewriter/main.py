class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        pre = "a"
        sum1 = 0
        
        for i in word:
            L = abs((ord(i)-ord(pre)))
            sum1 += min(L,26-L)
            pre = i

        return sum1 + len(word)
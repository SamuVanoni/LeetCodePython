class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        dic = {}
        for i in words:
            dic[i[-1]] = i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.split()
        r = []

        for i in range(k):
            r.append(s[i])
        
        return ' '.join(map(str, r))
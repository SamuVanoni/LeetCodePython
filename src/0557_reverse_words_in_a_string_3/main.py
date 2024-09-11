class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        words = s.split()
        for word in words:
            ans.append(word[len(word)::-1])
        return ' '.join(ans)
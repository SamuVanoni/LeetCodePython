class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        for i,c in enumerate(word):
            if c == ch:
                return word[i::-1] + word[i+1::]
        return word
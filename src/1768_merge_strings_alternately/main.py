class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        count = 0
        while len(word1) > count or len(word2) > count:
            if len(word1) > count:
                ans += word1[count]
            if len(word2) > count:
                ans += word2[count]
            count += 1
        return ans
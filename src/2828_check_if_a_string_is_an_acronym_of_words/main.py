class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        compare = ""
        for word in words:
            compare += word[0]
        return compare == s
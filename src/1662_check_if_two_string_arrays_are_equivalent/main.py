class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        concat = "".join(word1)
        concat2 = "".join(word2)
        if concat == concat2:
            return True
        return  False
        #return "".join(word1) == "".join(word2)
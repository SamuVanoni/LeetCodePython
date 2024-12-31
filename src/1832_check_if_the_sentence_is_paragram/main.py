class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        for letter in range(ord('a'), ord('z') + 1):
            if not chr(letter) in sentence:
                return False
        return True
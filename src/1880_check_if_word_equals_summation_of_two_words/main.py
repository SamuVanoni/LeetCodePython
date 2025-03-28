class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        sum = 0

        aux = ""
        for l in firstWord:
            aux += str(ord(l) - ord('a'))
        sum = int(aux)

        aux = ""
        for l in secondWord:
            aux += str(ord(l) - ord('a'))
        sum += int(aux)

        aux = ""
        for l in targetWord:
            aux += str(ord(l) - ord('a'))
        return int(aux) == sum
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count = 1
        countMax = 0
        for i in range(len(sentences)):
            for j in range(len(sentences[i])):
                if sentences[i][j] == " ":
                    count += 1
            if count > countMax:
                countMax = count
            count = 1
        return countMax
        #return max(len(word.split()) for word in sentences)
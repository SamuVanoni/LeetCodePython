class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i, word in enumerate(words):
            for j in range(i + 1, len(words)):
                if word == words[j][::-1]:
                    count += 1
        return count
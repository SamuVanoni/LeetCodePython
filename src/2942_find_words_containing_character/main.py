class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
        # counts = []
        # sentinel = False
        # for i, word in enumerate(words):
        #     for j in range(len(word)):
        #         if word[j] == x and not sentinel:
        #             counts.append(i)
        #             sentinel = True
        #     sentinel = False
        # return counts
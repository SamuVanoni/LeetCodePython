class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        a = " ".join(words)

        return a.replace(separator," ").split()

        # ans=[]

        # for word in words:
        #     for i in word.split(separator):
        #         if i: # Check if the split word is not empty.
        #             ans.append(i)

        # return ans 
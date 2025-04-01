class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for letter in words[0]:
            find = True

            for i in range(1, len(words)):
                if not letter in words[i]:
                    find = False
                    break

            if find:
                for i in range(1, len(words)):
                    words[i] = words[i].replace(letter, "", 1)
                ans.append(letter)
        return ans
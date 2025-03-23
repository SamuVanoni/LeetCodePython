class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        freq = {}
        s1 = s1.split()
        s2 = s2.split()
        for word in s1:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        for word in s2:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        ans = []
        for i, j in freq.items():
            if j == 1:
                ans.append(i)
        return ans
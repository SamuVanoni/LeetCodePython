from collections import defaultdict

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def find(w):  # function that calculates the numeric pattern
            l = []
            m = defaultdict(int)
            i = 0
            for c in w:
                if c in m:
                    l.append(m[c])
                else:
                    i += 1
                    m[c] = i
                    l.append(m[c])
            return l

        ans = []
        pfind = find(pattern)
        for w in words:
            wfind = find(w)
            if wfind == pfind: 
                ans.append(w)
        return ans

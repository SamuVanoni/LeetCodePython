class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0

        for i in range(len(words)):
            s1 = words[i]

            for j in range(i+1, len(words)):
                s2 = words[j]

                if len(s1) > len(s2):
                    continue
                    
                pre = s2[:len(s1)]
                suf = s2[-len(s1):]
                if pre == s1 and suf == s1:
                    ans += 1

        return ans
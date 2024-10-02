class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ans = 0
        for s in words:
            if s.startswith(pref):
                ans += 1
        return ans
        
        # ans = 0
        # for word in words:
        #     count = 0
        #     for i in range(len(pref)):
        #         if len(word) < len(pref):
        #             break
        #         if word[i] == pref[i]:
        #             count += 1
        #     if count == len(pref):
        #         ans += 1
        #     count = 0
        # return ans
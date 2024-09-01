class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = ""
        count = 0
        for i in range(len(indices)):
            for j in range(len(indices)):
                if indices[j] == count:
                    ans += s[j]
                    count += 1
        return ans
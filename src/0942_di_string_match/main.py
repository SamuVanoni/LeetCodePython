class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = []
        c1 = len(s)
        c2 = 0
        for l in s:
            if l == 'D':
                ans.append(c1)
                c1 -= 1
            else:
                ans.append(c2)
                c2 += 1
        ans.append(c2)
        return ans
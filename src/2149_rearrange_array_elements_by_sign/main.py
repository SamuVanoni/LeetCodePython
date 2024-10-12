class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = [n for n in nums if n >= 0]
        n = [n for n in nums if n < 0]
        ans = []
        for i in range(len(nums) / 2):
            ans.append(p[i])
            ans.append(n[i])
        return ans
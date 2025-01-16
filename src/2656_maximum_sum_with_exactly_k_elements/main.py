class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = max(nums)
        ans = 0
        while k > 0:
            k -= 1
            ans += m + k
        return ans
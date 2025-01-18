class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        l = len(nums)
        for i in range(l):
            if l % (i+1) == 0:
                ans += nums[i] * nums[i]
        return ans
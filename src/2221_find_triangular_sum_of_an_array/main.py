class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = []
        while n > 1:
            for i in range(len(nums) - 1):
                ans.append((nums[i] + nums[i+1]) % 10)
            nums = ans
            ans = []
            n -= 1
        return nums[0]
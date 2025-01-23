class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] - nums[i] + 1
                ans += diff
                nums[i] += diff
        return ans
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            ans.append(count)
        return ans
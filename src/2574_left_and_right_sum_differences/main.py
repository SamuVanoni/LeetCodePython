class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = [0]
        count = 0
        for i in range(len(nums) - 1):
            count += nums[i]
            leftSum.append(count)

        rightSum = [0]
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            count += nums[i]
            rightSum.insert(0, count)
        
        ans = []
        for i in range(len(leftSum)):
            ans.append(abs(leftSum[i] - rightSum[i]))
        return ans
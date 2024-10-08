class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if(num + nums[j] < target):
                    ans += 1
        return ans
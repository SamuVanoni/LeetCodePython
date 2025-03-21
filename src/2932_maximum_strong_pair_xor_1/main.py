class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x = 0
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    x = nums[i] ^ nums[j]
                if x > ans:
                    ans = x
        return ans
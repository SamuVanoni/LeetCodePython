class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = Counter(nums)
        ans = sum(i for i in nums if n[i] == 1)
        
        return ans
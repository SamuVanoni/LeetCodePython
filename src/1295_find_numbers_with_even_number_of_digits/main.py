class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans
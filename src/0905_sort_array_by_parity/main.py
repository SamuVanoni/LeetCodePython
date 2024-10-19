class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(num)
        for num in nums:
            if num % 2 == 1:
                ans.append(num)
        return ans
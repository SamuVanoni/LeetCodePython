class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            ans.append(n)
        for n in nums:
            ans.append(n)
        return ans # return nums + nums
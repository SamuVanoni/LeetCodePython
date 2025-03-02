class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        c = Counter(nums)
        return next((num for num, quant in c.items() if quant == n), None)
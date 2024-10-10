class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        return [n for n in nums if n < pivot] + [n for n in nums if n == pivot] + [n for n in nums if n > pivot]
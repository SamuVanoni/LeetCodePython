class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countP = 0
        countN = 0
        for n in nums:
            if n > 0:
                countP += 1
            if n < 0:
                countN += 1
        return max(countP, countN)
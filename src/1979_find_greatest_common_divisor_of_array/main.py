class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi, ma  = min(nums), max(nums)
        for i in range(mi, 0, -1):
            if mi % i == 0:
                if ma % i == 0:
                    return i
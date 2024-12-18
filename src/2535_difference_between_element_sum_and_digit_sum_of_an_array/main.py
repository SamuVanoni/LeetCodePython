class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1 = 0
        r2 = 0
        for n in nums:
            r1 += n
            r2 += sum(int(digit) for digit in str(n))
        return abs(r1 - r2)
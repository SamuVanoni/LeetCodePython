class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count1 = 0
        count2 = 0
        for n in nums:
            if n < 10:
                count1 += n
            else:
                count2 += n
        if count1 == count2:
            return False
        return True
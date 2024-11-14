class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        maxValue = max(d.values())  # Find max value
        # Return all values = maxValue
        return [r for r, value in d.items() if value == maxValue] 

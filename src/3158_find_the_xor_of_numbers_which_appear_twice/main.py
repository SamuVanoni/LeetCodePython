class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        twice = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    twice.append(nums[i])

        if not twice:
            return 0
        return reduce(lambda x, y: x ^ y, twice)
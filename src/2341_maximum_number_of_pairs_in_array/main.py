class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        countPairs = 0
        countRest = 0
        for value in freq.values():
            countPairs += (value // 2)
            if value % 2 == 1:
                countRest += 1
        
        return [countPairs, countRest]
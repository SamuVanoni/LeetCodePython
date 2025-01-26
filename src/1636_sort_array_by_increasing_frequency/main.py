class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums) # Counter({1: 3, -6: 2, 4: 2, 5: 1, -1: 1})
        return sorted(nums, key=lambda x: (freq[x], -x))
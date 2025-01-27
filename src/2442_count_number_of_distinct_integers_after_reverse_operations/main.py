class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        for i in range(l): # Add the reverse in the list
            nums.append(int(str(nums[i])[::-1]))

        count = Counter(nums) # Grouping by nums

        return len(count)
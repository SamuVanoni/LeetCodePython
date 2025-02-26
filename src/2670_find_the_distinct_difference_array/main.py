class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # One liner
        # return [len(Counter(nums[:i + 1])) - len(Counter(nums[i + 1:])) for i in range(len(nums))]
        
        prefix = defaultdict(int) # Empty dict to count different elements
        suffix = Counter(nums) # Entire list initially (frequency)
        result = []

        for x in nums:
            prefix[x] += 1
            suffix[x] -= 1
            if suffix[x] == 0:
                del suffix[x]
            result.append(len(prefix) - len(suffix))

        return result
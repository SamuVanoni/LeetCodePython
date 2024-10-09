class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        count = 0
        ans = []
        while len(nums) > 1:
            ans.append((min(nums) + max(nums)) / 2.0)
            nums.remove(min(nums))
            nums.remove(max(nums))
            count += 1
        
        if nums: # If an unmatched element remains
            ans.append(float(nums[0]))

        return min(ans)
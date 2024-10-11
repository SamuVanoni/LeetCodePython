class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        l = len(nums)
        ans = 0
        for i in range(l-2) :
            for j in range(i+1, l-1) :
                if nums[j] - nums[i] == diff :
                    for k in range(j+1, l) :
                        if nums[k] - nums[j] == diff :
                            ans += 1
        return ans
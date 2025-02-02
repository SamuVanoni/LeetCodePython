class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(len(nums) - 1):
            l, r = 0, 0
            for j in range(0, i+1):
                l += nums[j]
            for k in range(i+1, len(nums)):
                r += nums[k]
                
            if (l - r) % 2 == 0:
                ans += 1
                print(str(l) + " - " + str(r))
        
        return ans
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        i = 0
        while i < len(nums) / 2:
            ans.append(str(nums[i]) + str(nums[len(nums) - i - 1]))
            i += 1
        if len(nums) % 2 == 1:
            ans.append(str(nums[i]))
        return sum(int(num) for num in ans)
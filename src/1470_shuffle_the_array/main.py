class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        count = 0
        ans = []
        while count < n:
            ans.append(nums[count])
            ans.append(nums[count + n])
            count += 1
        return ans
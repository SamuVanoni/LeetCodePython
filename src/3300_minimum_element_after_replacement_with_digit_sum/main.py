class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for n in nums:
            count = 0
            while n > 0:
                count += n % 10
                n = n // 10
            ans.append(count)
        return min(ans)
class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        # There is a property that says the maximum XOR is obtained by OR bit a bit of the list numbers
        for num in nums:
            ans |= num
        return ans
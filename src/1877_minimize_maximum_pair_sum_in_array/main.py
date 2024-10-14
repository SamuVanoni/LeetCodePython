class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = sorted(nums)
        ans = -1
        i = 0
        j = len(b)-1
        while i < j:
            if(b[i] + b[j] > ans):
                ans = b[i] + b[j]
            i+=1
            j-=1
        return ans
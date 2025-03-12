class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set() # Set to store seen elements
        ans = []
        
        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)
        
        return ans
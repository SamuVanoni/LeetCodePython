class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [0, 0]
        for n in nums1:
            if n in nums2:
                ans[0] += 1
        for n in nums2:
            if n in nums1:
                ans[1] += 1
        return ans
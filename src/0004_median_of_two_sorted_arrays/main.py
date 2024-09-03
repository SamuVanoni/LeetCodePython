class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        nums = nums1 + nums2
        nums.sort()
        
        if (m + n) % 2 == 0:
            x = (m + n) / 2
            return (nums[x-1] + nums[x]) / 2.0
        else:
            x = int(math.ceil((m + n) / 2))
            return nums[x]
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for num1 in nums1:
            count = 0
            while count < len(nums2):
                if num1 == nums2[count] and num1 not in ans:
                    ans.append(num1)
                count += 1
        return ans
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}
        for num1 in nums1:
            d[num1[0]] = num1[1]
        for num2 in nums2:
            if num2[0] not in d:
                d[num2[0]] = num2[1]
            else:
                d[num2[0]] += num2[1]
                
        # Dic => List
        result = [[key, value] for key, value in d.items()]
        # Order
        result.sort(key=lambda x: x[0])
        
        return result
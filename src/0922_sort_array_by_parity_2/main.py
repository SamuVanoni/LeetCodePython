class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pair = [num for num in nums if num % 2 == 0]
        odd = [num for num in nums if num % 2 == 1]
        i = 0
        ans = []
        while(i < len(pair)):
            ans.append(pair[i])
            ans.append(odd[i])
            i += 1
        return ans
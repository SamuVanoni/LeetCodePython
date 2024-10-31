class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i] * 2)
                nums[i+1] = 0
            else:
                ans.append(nums[i])
        ans.append(nums[len(nums) - 1])

        return move_zeros_to_end(ans)
    
def move_zeros_to_end(arr):
    result = [num for num in arr if num != 0]
    zeros_count = arr.count(0)
    result.extend([0] * zeros_count)
    return result
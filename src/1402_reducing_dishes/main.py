class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()
        ans = 0

        while len(satisfaction) > 0:
            sum = 0
            for i in range(len(satisfaction)):
                sum += satisfaction[i] * (i+1)
                
            if sum > ans:
                ans = sum
            satisfaction.remove(satisfaction[0])

        return ans
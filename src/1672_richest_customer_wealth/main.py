class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        countMax = 0
        for x in accounts:
            count = 0
            for y in x:
                count += y
            if count > countMax:
                countMax = count
        return countMax
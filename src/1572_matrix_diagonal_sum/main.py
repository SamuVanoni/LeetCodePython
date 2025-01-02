class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        l = len(mat)
        ans = 0
        for i in range(l):
            ans += mat[i][i]
            ans += mat[i][l-i-1]
        if l % 2 == 1: # Repeated number
            ans -= mat[l//2][l//2]
        return ans
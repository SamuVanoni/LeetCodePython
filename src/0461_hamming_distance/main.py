class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0

        max_len = max(len(bin(x)[2:]), len(bin(y)[2:]))
        bin1 = format(x, '0{}b'.format(max_len))
        bin2 = format(y, '0{}b'.format(max_len))

        for i in range(max_len):
            if bin1[i] != bin2[i]:
                ans += 1
        
        return ans
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(code)):
            if k == 0:
                ans.append(0)
            elif k > 0:
                sum = 0
                for j in range(1, k+1):
                    j += i
                    if j > len(code)-1:
                        j -= len(code)
                    sum += code[j]
                ans.append(sum)
            else:
                sum = 0
                for j in range(-1, k-1, -1):
                    j += i
                    if j < 0:
                        j = j + len(code)
                    sum += code[j]
                ans.append(sum)
        return ans
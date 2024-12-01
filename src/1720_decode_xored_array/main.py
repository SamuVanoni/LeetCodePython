class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        ans = [first]
        for i in range(len(encoded)):
            ans.append(ans[i] ^ encoded[i])
        return ans
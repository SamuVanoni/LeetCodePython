class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i in range(len(prices)):
            find = False
            j = i

            while not find and j < len(prices) - 1:
                j += 1
                if prices[j] <= prices[i]:
                    find = True
            
            if find:
                ans.append(prices[i] - prices[j])
            else:
                ans.append(prices[i])
        
        return ans
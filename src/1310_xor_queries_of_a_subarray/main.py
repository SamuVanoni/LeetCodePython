class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for q in queries:
            xor_sum = 0
            for i in range(q[0], q[1] + 1):
                xor_sum ^= arr[i]
            result.append(xor_sum)
        return result

        # ans = []
        # for i in range(len(queries)):
        #     j, k = queries[i][0], queries[i][1]
        #     res = 0
        #     for l in range(j, k+1):
        #         res = res ^ arr[l]
        #     ans.append(res)
        # return ans
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        ar = [False] * len(arr)

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j] and ar[j] != True:
                    ar[i] = True
                    ar[j] = True

        indices_distinct = [i for i, valor in enumerate(ar) if not valor]

        if k <= len(indices_distinct):
            return arr[indices_distinct[k - 1]]
        else:
            return ""
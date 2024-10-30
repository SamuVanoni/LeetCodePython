class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=[]
        s=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a=arr[i]
                b=arr[j]
                c=a/float(b)
                l.append(c) # [0.5, 0.3333333333333333, 0.2, 0.6666666666666666, 0.4, 0.6]
                s.append([a,b]) # [[1, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 5]]

        d=dict(zip(l,s)) # Link one list to another
        # {0.5: [1, 2], 0.2: [1, 5], 0.4: [2, 5], 0.6: [3, 5], 0.3333333333333333: [1, 3], 0.6666666666666666: [2, 3]}

        l.sort() # [0.2, 0.3333333333333333, 0.4, 0.5, 0.6, 0.6666666666666666]

        return d[l[k-1]]
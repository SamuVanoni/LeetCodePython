class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        ans = []
        m = list(range(1, m + 1))
        for q in queries:
            i = m.index(q)
            ans.append(i)
            m.insert(0, m.pop(i))  # Remove and insert at the beginning
        return ans
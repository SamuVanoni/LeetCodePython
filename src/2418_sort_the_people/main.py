class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(names)

        mapping = {}
        for i in range(n):
            mapping[heights[i]] = names[i]

        heights.sort(reverse=True)
        for i in range(n):
            h = heights[i]
            names[i] = mapping[h]

        return names
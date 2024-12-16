class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        ans = 0
        for garb in garbage:
            for letter in garb:
                ans += 1

        # Find the last occurrence
        find = {'G': -1, 'P': -1, 'M': -1}
        for i in range(len(garbage) - 1, -1, -1):
            if 'G' in garbage[i] and find['G'] == -1:
                find['G'] = i
            if 'P' in garbage[i] and find['P'] == -1:
                find['P'] = i
            if 'M' in garbage[i] and find['M'] == -1:
                find['M'] = i

        for key, index in find.items():
            if index != -1:
                ans += sum(travel[:index]) # Sum the travel time to the found index

        return ans
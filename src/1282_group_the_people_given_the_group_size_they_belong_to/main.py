class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        group_map = {}
        for i, size in enumerate(groupSizes):
            if size in group_map:
                group_map[size].append(i)
            else:
                group_map[size] = [i]
        
        #print(group_map) {1: [5], 3: [0, 1, 2, 3, 4, 6]}
        result = []
        for size, group in group_map.items(): # 1 - [5] / 3 - [0, 1, 2, 3, 4, 6]
            for i in range(0, len(group), size):
                result.append(group[i:i+size])
        
        return result
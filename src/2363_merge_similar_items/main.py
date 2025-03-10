class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        freq = {}
        for i in items1:
            if i[0] not in freq:
                freq[i[0]] = i[1]
            else:
                freq[i[0]] += i[1]

        for i in items2:
            if i[0] not in freq:
                freq[i[0]] = i[1]
            else:
                freq[i[0]] += i[1]
        
        return sorted([[k, v] for k, v in freq.items()])
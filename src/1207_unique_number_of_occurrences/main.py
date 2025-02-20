class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        frequencies = {}
        for num in arr:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        # .set() => Join the repeated .values()
        return len(set(frequencies.values())) == len(frequencies.values())
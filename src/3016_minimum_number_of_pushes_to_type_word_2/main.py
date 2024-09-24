class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = Counter(word).values()
        sorted_freq = sorted(freq, reverse=True)
        result = i = 0

        for n in sorted_freq:
            result += n * (i // 8 + 1)
            i += 1
        
        return result
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print(Counter(s).values())
        print(set(Counter(s).values()))
        print(len(set(Counter(s).values())))
        return len(set(Counter(s).values())) == 1
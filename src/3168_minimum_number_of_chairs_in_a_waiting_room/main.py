class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxCount = 0
        for letter in s:
            if letter == "E":
                count += 1
            if letter == "L":
                count -= 1
            if maxCount < count:
                maxCount = count
        return maxCount
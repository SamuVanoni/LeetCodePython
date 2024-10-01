class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = 'aeiouAEIOU'
        count = 0
        count1 = 0
        count2 = 0
        middle = len(s) / 2
        while(count < middle):
            if s[count] in string:
                count1 += 1
            if s[len(s) - count - 1] in string:
                count2 += 1
            count += 1
        return count1 == count2
class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        base = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for l in s:
            if l in base:
                vowels.append(l)
        vowels.sort()

        result = []
        count = 0
        for l in s:
            if l in base:
                result.append(vowels[count])
                count += 1
            else:
                result.append(l)
        
        return ''.join(result)
class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        result = []
        s = ""

        for c in target:
            s += 'a'
            result.append(s)

            while s[-1] != c:
                last_char = s[-1]
                last_char = chr(ord(last_char) + 1) if last_char != 'z' else 'a'
                s = s[:-1] + last_char
                result.append(s)

        return result
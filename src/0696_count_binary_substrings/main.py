class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # Add the last group
        # print(groups) => [2, 2, 2, 2] two 0, two 1, two 0, two 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])  # Form pairs with groups

        return ans
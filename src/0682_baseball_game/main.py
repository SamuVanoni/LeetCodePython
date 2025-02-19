class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = []
        for op in operations:
            if op == '+':
                ans.append(ans[-1] + ans[-2])
            elif op == 'D':
                ans.append(ans[-1] * 2)
            elif op == 'C':
                del ans[-1]
            else:
                ans.append(int(op))
        return sum(ans)
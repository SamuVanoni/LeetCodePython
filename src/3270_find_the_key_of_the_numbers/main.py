class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        def padding(num):
            st = str(num)
            while len(st) < 4:
                st = "0" + st
            return st

        p = padding(num1)
        q = padding(num2)
        r = padding(num3)

        ans = ""
        for i in range(4):
            ans += str(min(int(p[i]), int(q[i]), int(r[i])))
        return int(ans)
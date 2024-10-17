class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack = []
        for ch in s:
            if ch == '[': # If = '[' add to stack
                stack.append(ch)
            else:
                if stack: # If = ']' and there is already '[' in the stack, remove 1 element
                    stack.pop()
                else: # Count one if you don't have a stack
                    count += 1
        return int(ceil(count / 2.0))
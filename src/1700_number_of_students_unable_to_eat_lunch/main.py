class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        ans = len(sandwiches)
        for s in sandwiches:
            if s in students:
                ans -= 1
                students.remove(s)
            else:
                break
        return ans
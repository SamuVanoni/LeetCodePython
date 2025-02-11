class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        count = 0
        for i in range(len(seats)):
            count += abs(seats[i] - students[i])
        return count
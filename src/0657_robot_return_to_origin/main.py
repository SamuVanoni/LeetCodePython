class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        freq = {
            "R": 0,
            "L": 0,
            "U": 0,
            "D": 0
        }

        for letter in moves:
            freq[letter] += 1

        if freq["R"] == freq["L"] and freq["U"] == freq["D"]:
            return True
        return False

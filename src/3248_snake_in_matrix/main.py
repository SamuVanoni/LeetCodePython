class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        i = 0
        j = 0

        # Dictionary for mapping commands to movement functions
        c = {
            "RIGHT": lambda i, j: (i, j + 1),
            "LEFT": lambda i, j: (i, j - 1),
            "DOWN": lambda i, j: (i + 1, j),
            "UP": lambda i, j: (i - 1, j)
        }

        for command in commands:
            # Get the corresponding function and update (i, j)
            if command in c:
                i, j = c[command](i, j)
            else:
                return "Error"

        matrix = create_matrix(n)
        return matrix[i][j]

def create_matrix(n):
    # Initialize
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix with values ​​from 0 to n*n - 1
    value = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = value
            value += 1

    return matrix
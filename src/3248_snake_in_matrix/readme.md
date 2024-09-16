## What Did I Learn?

### In this challenge I learned how to reduce the number of if and else using a dictionary with integration of lambdas functions. And creating a matrix in python:

1. A dictionary that executes a lambda function for parameters i and j according to the user's choice
```python
c = {
    "RIGHT": lambda i, j: (i, j + 1),
    "LEFT": lambda i, j: (i, j - 1),
    "DOWN": lambda i, j: (i + 1, j),
    "UP": lambda i, j: (i - 1, j)
}
```

2. If command is in the c dictionary it will execute the lambda and store the values ​​i and j
```python
if command in c:
    i, j = c[command](i, j)
else:
    return "Error"
```

3. Function used to create an matrix with numbers from `0` to `n x n - 1`
```python
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    value = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = value
            value += 1

    return matrix
```
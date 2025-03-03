## What Did I Learn?

### In this challenge I learned:

1. Reversing the matrix: Exchanging the order of the lines, putting the last line as first and so on.
```python
l = 0
r = len(matrix) -1
while l < r:
    matrix[l], matrix[r] = matrix[r], matrix[l]
    l += 1
    r -= 1
```

2. Transposing the matrix: rows become columns, columns become rows.
```python
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
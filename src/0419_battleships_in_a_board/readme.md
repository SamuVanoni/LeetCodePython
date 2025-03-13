## What Did I Learn?

### In this challenge I learned:

1. Creating a condition to add +1 to the answer. Check if the left and above are ".".
```python
if (i == 0 or board[i - 1][j] == ".") and\
   (j == 0 or board[i][j - 1] == "."):
```
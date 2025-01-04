## What Did I Learn?

### In this challenge I learned:

1. Looping from left and if the number of numbers is odd, we will perform the if
```python
for right in range(left, n):
    if (right - left + 1) % 2 == 1:
```

2. It will add the numbers from left to right
```python
current_sum = 0
for index in range(left, right + 1):
    current_sum += arr[index]
answer += current_sum
```
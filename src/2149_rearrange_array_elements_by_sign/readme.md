## What Did I Learn?

### In this challenge I put into practice a new way of solving problems:

1. We create two different arrays, one with positive values ​​and the other with negative values.
```python
p = [n for n in nums if n >= 0]
n = [n for n in nums if n < 0]
```

2. After that we create the answer by interleaving the elements of each array.
```python
for i in range(len(nums) / 2):
    ans.append(p[i])
    ans.append(n[i])
```
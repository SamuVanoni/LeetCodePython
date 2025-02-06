## What Did I Learn?

### In this challenge I learned:

1. Make a circular list increasing
```python
sum = 0
for j in range(1, k+1):
    j += i
    if j > len(code)-1:
        j -= len(code)
    sum += code[j]
ans.append(sum)
```

2. Make a circular list decreasing
```python
sum = 0
for j in range(-1, k-1, -1):
    j += i
    if j < 0:
        j += len(code)
    sum += code[j]
ans.append(sum)
```
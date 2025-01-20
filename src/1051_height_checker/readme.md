## What Did I Learn?

### In this challenge I learned:

1. aux is a copy of the list heights ([:])
```python
aux = heights[:]
```

2. We count the numbers that are different between aux and heights
```python
for i in range(len(heights)):
    if aux[i] != heights[i]:
        ans += 1
```

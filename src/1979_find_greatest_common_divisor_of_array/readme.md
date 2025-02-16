## What Did I Learn?

### In this challenge I learned:

1. Making a smaller loop up to 1
```python
for i in range(mi, 0, -1):
```

2. If the rest by dividing the smallest number and the largest is 0, we return the value
```python
if mi % i == 0:
    if ma % i == 0:
        return i
```
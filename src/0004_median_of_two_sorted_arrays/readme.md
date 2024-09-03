## What Did I Learn?

### In this challenge I learned more about logic:

1. If the number of elements in the array is a multiple of 2, we take the 2 in the middle and take the average
```python
if (m + n) % 2 == 0:
    x = (m + n) / 2
    return (nums[x-1] + nums[x]) / 2.0
```

2. If the number of elements is odd, we only take the middle one
```python
else:
    x = int(math.ceil((m + n) / 2))
    return nums[x]
```
## What Did I Learn?

### In this challenge I learned:

1. Remembering how to add and change elements in a dict
```python
freq = {}
for i in range(len(nums)):
    if nums[i] not in freq:
        freq[nums[i]] = 1
    else:
        freq[nums[i]] += 1
```

2. Taking only the values ​​of the dict
```python
freq.values()
```
## What Did I Learn?

### In this challenge I learned:

1. Empty dict to count different elements
```python
prefix = defaultdict(int)
```

2. Counts the frequency of the elements in the suffix (the entire list initially)
```python
suffix = Counter(nums)
```

3. Add elements on the empty list and removing from the full list
```python
for x in nums:
    prefix[x] += 1
    suffix[x] -= 1
    if suffix[x] == 0:
        del suffix[x]
```

4. Add the resulting one by one in the result list
```python
result.append(len(prefix) - len(suffix))
```
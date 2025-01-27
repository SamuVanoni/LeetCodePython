## What Did I Learn?

### In this challenge I learned:

1. Add the reverse in the list
```python
for i in range(l):
    nums.append(int(str(nums[i])[::-1]))
```

2. Grouping by nums and counting
```python
count = Counter(nums)
return len(count)
```
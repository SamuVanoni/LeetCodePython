## What Did I Learn?

### In this challenge I lerned more about logic:

1. We start by sorting in descending order to save time
```python
nums.sort(reverse=True)
```

2. Then we see its negative number is also in the array, if so, return
```python
if -nums[i] in nums:
    return nums[i]
```
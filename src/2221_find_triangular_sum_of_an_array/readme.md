## What Did I Learn?

### In this challenge I learned:

1. Loop that repeats until only one element is left on the list
```python
n = len(nums)
while n > 1:
    n -= 1
```

2. Creating a new list with the sum of the elements of the previous one and updating values
```python
ans = []
while n > 1:
    for i in range(len(nums) - 1):
        ans.append((nums[i] + nums[i+1]) % 10)
    nums = ans
    ans = []
    n -= 1
return nums[0]
```
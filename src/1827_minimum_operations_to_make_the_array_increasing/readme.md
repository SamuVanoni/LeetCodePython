## What Did I Learn?

### In this challenge I learned:

1. Instead of doing a while loop with an increment and decrement of 1 by 1, we do an IF with the total increment and decrement, calculated using the diff variable.
```python
if nums[i] <= nums[i-1]:
    diff = nums[i-1] - nums[i] + 1
    ans += diff
    nums[i] += diff
```

## What Did I Learn?

### In this challenge I learned how to manipulate Python loops with more control:

1. Performing 3 loops without repeating the list elements
```python
l = len(nums)
for i in range(l-2) :
    for j in range(i+1, l-1) :
        for k in range(j+1, l) :
```
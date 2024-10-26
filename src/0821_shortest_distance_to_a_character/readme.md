## What Did I Learn?

### In this challenge I learned more about lists:

1. We start by looping from left to right adding the distance values ​​into the response array
```python
for i in range(len(s)):
    if s[i] == c:
        count = 0
    else:
        count += 1
    ans[i] = count

print(ans) # [inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]
```
If you did not find any value = c we store 'inf' in the location

2. Then we loop from right to left, changing if there is a smaller value in the distance to = c and completing the 'inf'
```python
for i in range(len(s) - 1, -1, -1):
    if s[i] == c:
        count = 0
    else:
        count += 1
    ans[i] = min(ans[i], count)  # Lowest value
```
## What Did I Learn?

### In this challenge I learned more about logic:

1. Swapping the last element with the first until you reach the middle of the list
```python
while l > count:
    s[count], s[l] = s[l], s[count]
    count += 1
    l -= 1
```